#!/usr/bin/env python3
"""Copy the guide and product texts from the Hugging Face dataset repo into docs/.

The texts are built daily from the shop's own pages and pushed to Hugging Face (guides/);
this script mirrors that folder into docs/ for GitHub Pages. Standard library + git.
Sold pieces disappear from guides/products/ and are removed from docs/products/ here.
"""
import os
import shutil
import subprocess
import sys
import tempfile

REPO = "https://huggingface.co/datasets/kitanesque/kitanesque-vintage-sizing"
MIN_GUIDES, MIN_PRODUCTS = 9, 50   # 8 guides + README.md; index.md does not count as a product


def md_files(d):
    return sorted(n for n in os.listdir(d) if n.endswith(".md")) if os.path.isdir(d) else []


def check(path):
    with open(path, "rb") as f:
        head = f.read(4)
    return head.startswith(b"---") and os.path.getsize(path) >= 300


def main():
    tmp = tempfile.mkdtemp()
    env = dict(os.environ, GIT_LFS_SKIP_SMUDGE="1")
    subprocess.run(["git", "clone", "--depth", "1", "--quiet", REPO, tmp], check=True, env=env)
    src, src_p = os.path.join(tmp, "guides"), os.path.join(tmp, "guides", "products")
    guides, products = md_files(src), md_files(src_p)
    if len(guides) < MIN_GUIDES:
        sys.exit(f"only {len(guides)} guide files on Hugging Face - nothing written")
    bad = [n for n in guides if not check(os.path.join(src, n))] + \
          [n for n in products if not check(os.path.join(src_p, n))]
    if bad:
        sys.exit(f"unexpected content in {bad[:5]} - nothing written")
    pieces = [n for n in products if n != "index.md"]
    have = [n for n in md_files(os.path.join("docs", "products")) if n != "index.md"]
    if "README.md" not in guides or "index.md" not in products or len(pieces) < MIN_PRODUCTS:
        sys.exit(f"incomplete copy on Hugging Face ({len(guides)} guide files, {len(pieces)} pieces) - nothing written")
    if len(pieces) < 0.5 * len(have) and os.environ.get("ALLOW_DROP") != "1":
        sys.exit(f"product pages would fall from {len(have)} to {len(pieces)} - nothing written "
                 "(run the workflow by hand with allow_drop ticked to accept)")
    os.makedirs("docs", exist_ok=True)
    for n in guides:
        shutil.copyfile(os.path.join(src, n), os.path.join("docs", "index.md" if n == "README.md" else n))
    if len(products) >= MIN_PRODUCTS:
        dst = os.path.join("docs", "products")
        os.makedirs(dst, exist_ok=True)
        keep = set(products)
        for n in md_files(dst):
            if n not in keep:
                os.remove(os.path.join(dst, n))
        for n in products:
            shutil.copyfile(os.path.join(src_p, n), os.path.join(dst, n))
    else:
        print(f"only {len(products)} product files on Hugging Face - docs/products left as it is")
    print(f"{len(guides)} guide files and {len(products)} product files copied to docs/")


if __name__ == "__main__":
    main()
