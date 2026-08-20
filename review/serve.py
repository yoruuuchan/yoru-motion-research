#!/usr/bin/env python3
"""Serve the review console.

The preview media lives in sibling checkouts (locomotion-free/, video-shotcraft/),
so the server is rooted at the parent of this repository and the console is opened
at its path underneath. Opening index.html straight from disk does not work: the
dataset JSON is loaded with fetch(), which browsers block on file://.

    python review/serve.py
"""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import webbrowser
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO.parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8899)
    parser.add_argument("--root", default=str(ROOT), help="directory to serve (default: repo parent)")
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    url = f"http://127.0.0.1:{args.port}/{REPO.relative_to(root).as_posix()}/review/"

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", args.port), handler) as httpd:
        print(f"serving {root}\nconsole: {url}\nCtrl+C to stop")
        if not args.no_open:
            webbrowser.open(url)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
