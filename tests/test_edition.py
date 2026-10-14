#!/usr/bin/env python3
"""
The edition channel's publisher and verifier (model/edition.py, #111, #112), against a fake Storage server.

    python3 -m unittest discover -s tests -v

What must hold, with no network: an edition is uploaded under its id and never overwritten; a re-run of the
same edition changes nothing and passes; different bytes under the same id fail; latest.json moves last and
only when every part is served; the service-role key is never in a URL, on stdout or in the summary; and
verify() fails, not passes, against a bucket that serves altered bytes or no pointer.
"""
from __future__ import annotations

import http.server
import io
import json
import os
import sys
import tempfile
import threading
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import edition  # noqa: E402

KEY = "service-role-key-that-must-never-leak"


def make_edition(out: Path, parts: dict[str, bytes] | None = None) -> Path:
    """A small edition on disk in the shape export_json.split_bundle() writes, with a bundle file whose
    sha256 is the edition id."""
    bundle = out / "eu27.json"
    bundle.write_bytes(b'{"schema_version": 2, "generated": "2026-10-15", "x": 1}\n')
    parts = parts or {"eu27.core.json": b'{"index": {}}', "eu27.NL.json": b'{"documents": {"NL": {}}}',
                      "eu27.DE.json": b'{"documents": {"DE": {}}}'}
    for name, data in parts.items():
        (out / name).write_bytes(data)
    manifest = {"schema_version": 2, "generated": "2026-10-15", "edition": edition.sha256(bundle.read_bytes()),
                "parts": {n: {"sha256": edition.sha256(d), "bytes": len(d)} for n, d in parts.items()}}
    (out / edition.MANIFEST).write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    return bundle


class FakeStorage(http.server.BaseHTTPRequestHandler):
    """Supabase Storage as the publisher sees it: public GET, authorised POST, 400 Duplicate without upsert."""
    objects: dict[str, tuple[bytes, dict[str, str]]] = {}
    log: list[tuple[str, str]] = []               # (method, path) in order
    urls: list[str] = []
    PUBLIC = f"/storage/v1/object/public/{edition.BUCKET}/"
    OBJECT = f"/storage/v1/object/{edition.BUCKET}/"

    def _send(self, code: int, body: bytes, headers: dict[str, str] | None = None) -> None:
        self.send_response(code)
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa: N802
        self.urls.append(self.path)
        self.log.append(("GET", self.path))
        if not self.path.startswith(self.PUBLIC):
            return self._send(404, b"")
        key = self.path[len(self.PUBLIC):]
        if key not in self.objects:
            return self._send(400, b'{"statusCode":"404","error":"not_found","message":"Object not found"}')
        data, headers = self.objects[key]
        return self._send(200, data, {"cache-control": headers.get("cache-control", "")})

    def do_POST(self):  # noqa: N802
        self.urls.append(self.path)
        self.log.append(("POST", self.path))
        if self.headers.get("Authorization") != f"Bearer {KEY}":
            return self._send(401, b'{"statusCode":"401","error":"Unauthorized"}')
        key = self.path[len(self.OBJECT):]
        data = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if key in self.objects and self.headers.get("x-upsert", "false") != "true":
            return self._send(400, b'{"statusCode":"409","error":"Duplicate","message":"The resource already exists"}')
        self.objects[key] = (data, {"cache-control": self.headers.get("cache-control", "")})
        return self._send(200, b'{"Key":"' + key.encode() + b'"}')

    def log_message(self, *args):  # noqa: ANN002
        pass


class Server:
    def __enter__(self):
        FakeStorage.objects, FakeStorage.log, FakeStorage.urls = {}, [], []
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), FakeStorage)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_port}"
        self.public = f"{self.url}/storage/v1/object/public/{edition.BUCKET}"
        return self

    def __exit__(self, *exc):  # noqa: ANN002
        self.server.shutdown()


def run_publish(dir_: Path, bundle: Path, url: str, commit: str = "abc1234") -> tuple[int, str, str]:
    """edition.py publish as the workflow runs it; returns exit code, stdout and the summary file."""
    with tempfile.TemporaryDirectory() as tmp:
        summary = Path(tmp) / "summary.md"
        out = io.StringIO()
        with mock.patch.dict(os.environ, {"SUPABASE_URL": url, "SUPABASE_SERVICE_ROLE_KEY": KEY}), redirect_stdout(out):
            code = edition.main(["publish", "--dir", str(dir_), "--bundle", str(bundle), "--commit", commit,
                                 "--run-id", "7", "--run-url", "https://example.invalid/runs/7",
                                 "--summary", str(summary)])
        return code, out.getvalue(), summary.read_text(encoding="utf-8") if summary.exists() else ""


class Publish(unittest.TestCase):
    def test_a_first_publish_uploads_every_part_then_the_pointer(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            code, out, summary = run_publish(Path(tmp), bundle, s.url)
            self.assertEqual(code, 0, out)
            manifest = json.loads((Path(tmp) / edition.MANIFEST).read_text())
            ed = manifest["edition"]
            self.assertEqual(sorted(FakeStorage.objects), sorted([f"{ed}/{n}" for n in manifest["parts"]]
                                                                  + [f"{ed}/{edition.MANIFEST}", f"{ed}/{edition.PUBLISHED}",
                                                                     edition.LATEST]))
            posts = [p for m, p in FakeStorage.log if m == "POST"]
            self.assertTrue(posts[-1].endswith("/" + edition.LATEST), "latest.json must be written last")
            latest = json.loads(FakeStorage.objects[edition.LATEST][0])
            self.assertEqual(latest["edition"], ed)
            self.assertEqual(latest["commit"], "abc1234")
            self.assertEqual(FakeStorage.objects[f"{ed}/eu27.NL.json"][1]["cache-control"], edition.IMMUTABLE)
            self.assertEqual(FakeStorage.objects[edition.LATEST][1]["cache-control"], edition.POINTER)
            self.assertIn("| `" + ed + "` |", summary)
            self.assertIn("Edition published", summary)

    def test_a_re_run_changes_nothing_and_passes(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            self.assertEqual(run_publish(Path(tmp), bundle, s.url)[0], 0)
            before = {k: v[0] for k, v in FakeStorage.objects.items()}
            FakeStorage.log.clear()
            code, out, _ = run_publish(Path(tmp), bundle, s.url)
            self.assertEqual(code, 0, out)
            self.assertIn("already published, identical", out)
            part_posts = [p for m, p in FakeStorage.log if m == "POST" and not p.endswith(edition.LATEST)]
            self.assertEqual(part_posts, [], "an existing part is never re-uploaded")
            after = {k: v[0] for k, v in FakeStorage.objects.items()}
            self.assertEqual({k: v for k, v in before.items() if k != edition.LATEST},
                             {k: v for k, v in after.items() if k != edition.LATEST})

    def test_different_bytes_under_the_same_edition_id_fail_and_the_pointer_does_not_move(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            manifest = json.loads((Path(tmp) / edition.MANIFEST).read_text())
            ed = manifest["edition"]
            FakeStorage.objects[f"{ed}/eu27.NL.json"] = (b'{"documents": {"NL": {"tampered": true}}}', {})
            code, out, _ = run_publish(Path(tmp), bundle, s.url)
            self.assertEqual(code, 1)
            self.assertIn("different bytes", out)
            self.assertNotIn(edition.LATEST, FakeStorage.objects)

    def test_a_stale_tree_is_refused_before_anything_is_uploaded(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            (Path(tmp) / "eu27.DE.json").write_bytes(b"{}")      # edited after the manifest was written
            code, out, _ = run_publish(Path(tmp), bundle, s.url)
            self.assertEqual(code, 1)
            self.assertEqual(FakeStorage.objects, {})
            self.assertIn("FAIL part eu27.DE.json", out)

    def test_the_key_is_never_in_a_url_on_stdout_or_in_the_summary(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            code, out, summary = run_publish(Path(tmp), bundle, s.url)
            self.assertEqual(code, 0)
            self.assertNotIn(KEY, out)
            self.assertNotIn(KEY, summary)
            self.assertFalse(any(KEY in u for u in FakeStorage.urls))

    def test_without_the_key_nothing_is_uploaded(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            with mock.patch.dict(os.environ, {"SUPABASE_URL": s.url}, clear=False):
                os.environ.pop("SUPABASE_SERVICE_ROLE_KEY", None)
                with redirect_stdout(io.StringIO()), self.assertRaises(RuntimeError):
                    edition.main(["publish", "--dir", tmp, "--bundle", str(bundle)])
            self.assertEqual(FakeStorage.objects, {})


class Verify(unittest.TestCase):
    def test_a_published_edition_verifies(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            self.assertEqual(run_publish(Path(tmp), bundle, s.url)[0], 0)
            results = edition.verify(s.public, Path(tmp) / edition.MANIFEST)
            self.assertTrue(all(ok for _, ok, _ in results), results)
            self.assertEqual(len(results), 2 + 1 + 3)           # latest ×2, manifest, three parts

    def test_an_altered_part_fails_by_name(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            self.assertEqual(run_publish(Path(tmp), bundle, s.url)[0], 0)
            ed = json.loads((Path(tmp) / edition.MANIFEST).read_text())["edition"]
            data, headers = FakeStorage.objects[f"{ed}/eu27.DE.json"]
            FakeStorage.objects[f"{ed}/eu27.DE.json"] = (data + b" ", headers)
            failed = [n for n, ok, _ in edition.verify(s.public, Path(tmp) / edition.MANIFEST) if not ok]
            self.assertEqual(failed, ["served eu27.DE.json"])

    def test_a_missing_pointer_fails(self):
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            self.assertEqual(run_publish(Path(tmp), bundle, s.url)[0], 0)
            del FakeStorage.objects[edition.LATEST]
            results = {n: ok for n, ok, _ in edition.verify(s.public, Path(tmp) / edition.MANIFEST)}
            self.assertFalse(results[f"{edition.LATEST} names the committed edition"])

    def test_the_smoke_test_carries_the_channel(self):
        import smoke  # noqa: PLC0415
        with tempfile.TemporaryDirectory() as tmp, Server() as s:
            bundle = make_edition(Path(tmp))
            self.assertEqual(run_publish(Path(tmp), bundle, s.url)[0], 0)
            results = smoke.run("", None, 14, s.public, Path(tmp) / edition.MANIFEST)
            self.assertTrue(all(ok for _, ok, _ in results), results)
            self.assertTrue(all(n.startswith("edition ") for n, _, _ in results))
        results = smoke.run("", None, 14, "", None)
        self.assertEqual(results, [("edition channel", True, "not configured (SUPABASE_URL unset)")])


class Check(unittest.TestCase):
    def test_the_tree_check_passes_on_a_fresh_edition_and_names_what_is_wrong(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            bundle = make_edition(out)
            site = out / "site" / edition.MANIFEST
            site.parent.mkdir()
            site.write_bytes((out / edition.MANIFEST).read_bytes())
            self.assertTrue(all(ok for _, ok, _ in edition.check(out, bundle, site)))
            (out / "eu27.XX.json").write_bytes(b"{}")
            failed = {n for n, ok, _ in edition.check(out, bundle, site) if not ok}
            self.assertEqual(failed, {"no stray part"})
            (out / "eu27.XX.json").unlink()
            site.write_bytes(b"{}")
            failed = {n for n, ok, _ in edition.check(out, bundle, site) if not ok}
            self.assertEqual(failed, {"site manifest equals the app's"})

    def test_the_committed_tree_passes(self):
        results = edition.check(ROOT / "mobile" / "assets" / "data", ROOT / "web" / "public" / "data" / "eu27.json",
                                ROOT / "web" / "public" / "data" / "manifest.json")
        missing = [n for n, ok, d in results if not ok and "missing" in d]
        if missing:
            self.skipTest("parts not generated: run python3 model/export_json.py --split --from web/public/data/eu27.json")
        self.assertTrue(all(ok for _, ok, _ in results), [r for r in results if not r[1]])


if __name__ == "__main__":
    unittest.main()
