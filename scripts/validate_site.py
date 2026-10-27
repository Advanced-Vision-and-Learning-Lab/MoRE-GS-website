#!/usr/bin/env python3
"""Validate local links and required assets for the static MoRE-GS site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag in {"a", "link", "script", "img", "source", "video"}:
            value = values.get("href") or values.get("src")
            if value:
                self.links.append(value)
        if values.get("data-lightbox"):
            self.links.append(values["data-lightbox"])
        for attribute in ("data-base", "data-top", "poster"):
            if values.get(attribute):
                self.links.append(values[attribute])


def main():
    index = DIST / "index.html"
    parser = LinkParser()
    parser.feed(index.read_text(encoding="utf-8"))
    missing = []
    for link in sorted(set(parser.links)):
        parsed = urlparse(link)
        if parsed.scheme or link.startswith(("#", "mailto:")):
            continue
        target = DIST / parsed.path
        if not target.exists():
            missing.append(link)
    required = [
        "assets/MoRE-GS.pdf",
        "assets/MoRE-GS-supplementary.pdf",
        "assets/method.png",
        "assets/lego-forecast-loop.mp4",
        "assets/standup-horizon-loop.mp4",
        "assets/chicken-horizon-loop.mp4",
        "assets/printer-horizon-loop.mp4",
        "assets/horizon-results.png",
        "assets/long-horizon-results.png",
        "assets/router-visualization.png",
        "assets/slider-chicken-ode.png",
        "assets/slider-chicken-moregs.png",
    ]
    for relative in required:
        if not (DIST / relative).is_file():
            missing.append(relative)
    if missing:
        raise SystemExit("Missing site assets:\n" + "\n".join(sorted(set(missing))))
    print("PASS: MoRE-GS website links and required assets are present")


if __name__ == "__main__":
    main()
