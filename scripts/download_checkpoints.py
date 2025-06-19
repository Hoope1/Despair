"""Utility to download all model checkpoints."""

# mypy: ignore-errors

from __future__ import annotations

from pathlib import Path

import gdown

MODELS = [
    {
        "name": "TEED (teed_simplified.pth)",
        "url": "https://drive.google.com/uc?id=1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu",
        "out": Path("checkpoints/teed_simplified.pth"),
    },
    {
        "name": "DexiNed (dexined_checkpoint.pth)",
        "url": "https://drive.google.com/uc?id=1u3zrP5TQp3XkQ41RUOEZutnDZ9SdpyRk",
        "out": Path("checkpoints/dexined_checkpoint.pth"),
    },
    {
        "name": "TEED-Alt (teed_checkpoint.pth)",
        "url": "https://drive.google.com/uc?id=1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu",
        "out": Path("checkpoints/teed_checkpoint.pth"),
    },
]


def download_all() -> None:
    """Download all configured checkpoints."""
    Path("checkpoints").mkdir(exist_ok=True)

    for model in MODELS:
        if model["out"].exists():
            print(f"{model['out']} already exists – skipping.")
            continue
        print(f"Downloading {model['name']} ...")
        gdown.download(model["url"], str(model["out"]), quiet=False)


if __name__ == "__main__":
    download_all()
