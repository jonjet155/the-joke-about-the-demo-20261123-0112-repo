"""Entry for the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt. Standard library only, no network.
"""

import os

JOKE = "Agent fixed the crash. It deleted the demo."


def main() -> None:
    # The gate allows 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280, "joke out of bounds"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
