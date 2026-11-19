#!/usr/bin/env python3
"""Copy the guide texts from the Hugging Face dataset repo into docs/.

The shop's own host blocks some data-centre ranges, so this job does not fetch the shop.
A machine at the shop builds the texts daily and pushes them to Hugging Face (guides/);
this script mirrors that folder into docs/ for GitHub Pages. Standard library only.
"""
import json
import os
import sys
import urllib.request

REPO = "kitanesque/kitanesque-vintage-sizing"
API = f"https://huggingface.co/api/datasets/{REPO}/tree/main/guides"
RAW = f"https://huggingface.co/datasets/{REPO}/resolve/main/guides/"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "kitanesque-guides-mirror"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    names = [e["path"].split("/")[-1] for e in json.loads(get(API)) if e.get("type") == "file"]
    names = [n for n in names if n.endswith(".md")]
    if len(names) < 8:
        sys.exit(f"only {len(names)} guide files on Hugging Face - nothing written")
    files = {}
    for n in names:
        body = get(RAW + n)
        if len(body) < 800 or not body.startswith(b"---"):
            sys.exit(f"{n}: unexpected content ({len(body)} bytes) - nothing written")
        files["index.md" if n == "README.md" else n] = body
    os.makedirs("docs", exist_ok=True)
    for n, body in files.items():
        with open(os.path.join("docs", n), "wb") as f:
            f.write(body)
    print(f"{len(files)} files written to docs/")


if __name__ == "__main__":
    main()
