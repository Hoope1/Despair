#!/usr/bin/env python
"""Download and verify edge detection model weights."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Dict

import gdown

CHECKPOINTS: Dict[str, Dict[str, str]] = {
    "teed": {
        "url": "https://drive.google.com/uc?id=1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu",
        "file": "teed_simplified.pth",
        "sha256": "",
    },
    "dexined": {
        "url": "https://drive.google.com/uc?id=1u3zrP5TQp3XkQ41RUOEZutnDZ9SdpyRk",
        "file": "dexined_checkpoint.pth",
        "sha256": "",
    },
    "teed_alt": {
        "url": "https://drive.google.com/uc?id=1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu",
        "file": "teed_checkpoint.pth",
        "sha256": "",
    },
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
            print(f"Checksum mismatch for {path.name}: {digest} != {expected}")
            return False
    return True


def download(url: str, out: Path) -> bool:
    """Download file from Google Drive with error handling."""
    try:
        gdown.download(url, str(out), quiet=False)
        return True
    except Exception as exc:  # pragma: no cover - network
        print(f"Failed to download {url}: {exc}")
        return False


def ensure_weights(directory: Path, check_only: bool = False) -> None:
    """Ensure all weights exist in *directory*."""
    directory.mkdir(parents=True, exist_ok=True)
    for name, info in CHECKPOINTS.items():
        target = directory / info["file"]
        if check_only:
            if verify(target, info.get("sha256", "")):
                print(f"✓ {target.name} present")
            else:
                print(f"Missing {target.name}")
        else:
            if verify(target, info.get("sha256", "")):
                print(f"✓ {target.name} already up to date")
                continue
            print(f"Downloading {name} weights ...")
            if download(info["url"], target):
                if verify(target, info.get("sha256", "")):
                    print(f"✓ {target.name} downloaded")
                else:
                    print(f"Warning: checksum for {target.name} could not be verified")


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
    args = parse_args()
    ensure_weights(Path(args.target), check_only=args.check)


if __name__ == "__main__":  # pragma: no cover - script usage
    main()
