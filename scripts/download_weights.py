# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
#!/usr/bin/env python
"""Download and verify edge detection model weights."""
from __future__ import annotations

import argparse
import hashlib
import logging
from pathlib import Path
from typing import Dict

import gdown

from config import DEXINED_URL, TEED_ALT_URL, TEED_URL

CHECKPOINTS: Dict[str, Dict[str, str]] = {
    "teed": {"url": TEED_URL, "file": "teed_simplified.pth", "sha256": ""},
    "dexined": {"url": DEXINED_URL, "file": "dexined_checkpoint.pth", "sha256": ""},
    "teed_alt": {"url": TEED_ALT_URL, "file": "teed_checkpoint.pth", "sha256": ""},
}


def sha256sum(path: Path) -> str:
    """Calculate SHA-256 checksum of a file."""
    hash_obj = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


def verify(path: Path, expected: str) -> bool:
    """Verify file checksum if expected value is provided."""
    if not path.exists():
        return False
    if expected:
        digest = sha256sum(path)
        if digest != expected:
            logging.warning("Checksum mismatch for %s: %s != %s", path.name, digest, expected)
            return False
    return True


def download(url: str, out: Path) -> bool:
    """Download file from Google Drive with error handling."""
    try:
        gdown.download(url, str(out), quiet=False)
        return True
    except Exception as exc:  # pragma: no cover - network
        logging.error("Failed to download %s: %s", url, exc)
        return False


def ensure_weights(directory: Path, check_only: bool = False) -> None:
    """Ensure all weights exist in *directory*."""
    directory.mkdir(parents=True, exist_ok=True)
    for name, info in CHECKPOINTS.items():
        target = directory / info["file"]
        if check_only:
            if verify(target, info.get("sha256", "")):
                logging.info("%s present", target.name)
            else:
                logging.info("Missing %s", target.name)
        else:
            if verify(target, info.get("sha256", "")):
                logging.info("%s already up to date", target.name)
                continue
            logging.info("Downloading %s weights ...", name)
            if download(info["url"], target):
                if verify(target, info.get("sha256", "")):
                    logging.info("%s downloaded", target.name)
                else:
                    logging.warning("Checksum for %s could not be verified", target.name)


def parse_args() -> argparse.Namespace:
    """CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="only check that weights are present",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path("checkpoints"),
        help="directory for downloaded weights",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = parse_args()
    ensure_weights(Path(args.target), check_only=args.check)


if __name__ == "__main__":  # pragma: no cover - script usage
    main()
