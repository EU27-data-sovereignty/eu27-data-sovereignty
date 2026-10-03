#!/usr/bin/env python3
"""
A small, stdlib mutation audit (#92): change one thing in a module at a time and see whether the tests notice.

    python3 tests/tools/mutation_audit.py model/evidence.py tests.test_evidence tests.test_properties

Run it in a throwaway clone: it rewrites the module in place while it works and restores it at the end.
Mutations: a comparison flipped (< <=, > >=, == !=, in / not in), `and` / `or` swapped, a `not` dropped, a
number off by one, `True` / `False` swapped. A mutant is *killed* when the named tests fail; one that
survives is a behaviour no test pins down. mutmut was tried first and needs package imports, which this
project's path-based tests do not use.
"""
from __future__ import annotations

import ast
import concurrent.futures as cf
import copy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SWAP = {ast.Lt: ast.LtE, ast.LtE: ast.Lt, ast.Gt: ast.GtE, ast.GtE: ast.Gt, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq,
        ast.In: ast.NotIn, ast.NotIn: ast.In}


def sites(tree: ast.AST) -> list[tuple[str, int, int]]:
    """(kind, node index in walk order, line) for every mutable spot."""
    out = []
    for i, node in enumerate(ast.walk(tree)):
        if isinstance(node, ast.Compare) and type(node.ops[0]) in SWAP:
            out.append(("compare", i, node.lineno))
        elif isinstance(node, ast.BoolOp):
            out.append(("boolop", i, node.lineno))
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            out.append(("not", i, node.lineno))
        elif isinstance(node, ast.Constant) and type(node.value) is int and not isinstance(node.value, bool):
            out.append(("number", i, node.lineno))
        elif isinstance(node, ast.Constant) and isinstance(node.value, bool):
            out.append(("bool", i, node.lineno))
    return out


def mutate(tree: ast.AST, index: int) -> str:
    t = copy.deepcopy(tree)
    for i, node in enumerate(ast.walk(t)):
        if i != index:
            continue
        if isinstance(node, ast.Compare):
            node.ops[0] = SWAP[type(node.ops[0])]()
        elif isinstance(node, ast.BoolOp):
            node.op = ast.Or() if isinstance(node.op, ast.And) else ast.And()
        elif isinstance(node, ast.UnaryOp):
            return ast.unparse(_replace(t, node, node.operand))
        elif isinstance(node, ast.Constant) and isinstance(node.value, bool):
            node.value = not node.value
        elif isinstance(node, ast.Constant):
            node.value = node.value + 1
        break
    return ast.unparse(t)


def _replace(tree: ast.AST, old: ast.AST, new: ast.AST) -> ast.AST:
    for parent in ast.walk(tree):
        for field, value in ast.iter_fields(parent):
            if value is old:
                setattr(parent, field, new)
            elif isinstance(value, list):
                for k, item in enumerate(value):
                    if item is old:
                        value[k] = new
    return tree


def run_one(root: Path, module: str, source: str, tests: list[str]) -> bool:
    """True if the tests fail (the mutant is killed). Each mutant runs in its own copy of the tree."""
    work = Path(tempfile.mkdtemp(prefix="mut-"))
    try:
        shutil.copytree(root, work / "r", ignore=shutil.ignore_patterns(".git", "node_modules", "cache", ".v",
                                                                          ".venv", "mutants"), symlinks=True)
        (work / "r" / module).write_text(source, encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "unittest", "-q", *tests], cwd=work / "r",
                           capture_output=True, timeout=300)
        return r.returncode != 0
    except subprocess.TimeoutExpired:
        return True
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main() -> int:
    module, tests = sys.argv[1], sys.argv[2:]
    root = Path.cwd()
    tree = ast.parse((root / module).read_text(encoding="utf-8"))
    spots = sites(tree)
    print(f"{module}: {len(spots)} mutants; tests: {' '.join(tests)}", flush=True)
    survived = []
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(run_one, root, module, mutate(tree, i), tests): (kind, i, line)
                   for kind, i, line in spots}
        for f in cf.as_completed(futures):
            if not f.result():
                survived.append(futures[f])
    killed = len(spots) - len(survived)
    print(f"killed {killed} of {len(spots)} ({killed / len(spots):.0%}); survived {len(survived)}")
    for kind, _, line in sorted(survived, key=lambda s: s[2]):
        print(f"  survived: {kind} at line {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
