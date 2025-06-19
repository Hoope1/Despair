# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
from pathlib import Path

import gdown


class ModelManager:
    """Manages model downloads and loading"""

    def __init__(self, cache_dir="checkpoints"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def download_dexined_weights(self) -> str | None:
        """Download DexiNed pretrained weights from Google Drive."""
        url = "https://drive.google.com/uc?id=1u3zrP5TQp3XkQ41RUOEZutnDZ9SdpyRk"
        output_path = self.cache_dir / "dexined_checkpoint.pth"

        if output_path.exists():
            print("DexiNed weights already downloaded")
            return str(output_path)

        try:
            print("Downloading DexiNed weights...")
            gdown.download(url, str(output_path), quiet=False)
            print("DexiNed weights downloaded successfully")
            return str(output_path)
        except Exception as e:
            print(f"Failed to download DexiNed weights: {e}")
            print("Using simplified model instead")
            return None

    def download_teed_weights(self) -> str | None:
        """Download TEED weights from Google Drive."""
        url = "https://drive.google.com/uc?id=1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu"
        output_path = self.cache_dir / "teed_simplified.pth"

        if output_path.exists():
            print("TEED weights already downloaded")
            return str(output_path)

        try:
            print("Downloading TEED weights...")
            gdown.download(url, str(output_path), quiet=False)
            print("TEED weights downloaded successfully")
            return str(output_path)
        except Exception as e:
            print(f"Failed to download TEED weights: {e}")
            return None
