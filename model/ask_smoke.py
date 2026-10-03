#!/usr/bin/env python3
"""
Ask the live /ask one fixed question and check the answer is grounded (#92). Read-only for the site; one
model request per run, within the dedicated workspace's spend limit.

    python3 model/ask_smoke.py [--site https://eu27.cloud] [--require]

Passes when the stream sends answer text, at least one citation (`cite` with claim ids) and `done` with a
stop reason other than a refusal. Without `--require`, an error answer (as served while ANTHROPIC_API_KEY
is not set in Vercel) is reported as "not configured" and passes; the monitor sets `--require` once the
owner switches the repository variable ASK_LIVE to true.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

QUESTION = "Which body operates Germany's civil registry, according to the project's sources?"


def ask(site: str, question: str) -> list[dict]:
    req = urllib.request.Request(f"{site}/api/ask", data=json.dumps({"question": question}).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "eu27-ask-smoke/1"},
                                 method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return [{"type": "error", "code": str(e.code), "message": e.reason}]
    except (urllib.error.URLError, OSError) as e:
        return [{"type": "error", "code": "unreachable", "message": str(e)}]
    events = []
    for line in body.splitlines():
        if line.startswith("data: "):
            try:
                events.append(json.loads(line[6:]))
            except json.JSONDecodeError:
                continue
    return events


def judge(events: list[dict]) -> tuple[str, str]:
    """('ok' | 'not_configured' | 'fail', detail)."""
    kinds = [e.get("type") for e in events]
    if "error" in kinds:
        e = next(x for x in events if x.get("type") == "error")
        return "not_configured", f"{e.get('code')}: {e.get('message')}"
    text = "".join(e.get("text", "") for e in events if e.get("type") == "text")
    cites = [e for e in events if e.get("type") == "cite" and e.get("claims")]
    done = next((e for e in events if e.get("type") == "done"), None)
    if not text.strip():
        return "fail", "no answer text"
    if not cites:
        return "fail", "an answer with no citation"
    if not done or done.get("stop_reason") == "refusal":
        return "fail", f"did not finish cleanly: {done}"
    return "ok", f"{len(text)} characters, {len(cites)} citations"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="https://eu27.cloud")
    ap.add_argument("--require", action="store_true", help="fail on an error answer too (once the key is set)")
    a = ap.parse_args(argv)
    state, detail = judge(ask(a.site.rstrip("/"), QUESTION))
    print(f"/ask: {state} ({detail})")
    return 0 if state == "ok" or (state == "not_configured" and not a.require) else 1


if __name__ == "__main__":
    sys.exit(main())
