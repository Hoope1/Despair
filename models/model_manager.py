# SPDX-License-Identifier: MIT

from pathlib import Path

import gdown


class ModelManager:
    """Manages model downloads and loading"""

    def __init__(self, cache_dir="checkpoints"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def download_dexined_weights(self):
        """Download DexiNed pretrained weights from Google Drive"""
        # DexiNed weights URL from the GitHub page
        url = "https://drive.google.com/uc?id=1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu"
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

    def download_teed_weights(self):
        """Download TEED weights if available"""
        # TEED doesn't provide direct download links in the repository
        # Would need to train or request from authors
        output_path = self.cache_dir / "teed_checkpoint.pth"

        if output_path.exists():
            print("TEED weights already available")
            return str(output_path)

        print("TEED pretrained weights not available for direct download")
        print("Using randomly initialized weights (demo mode)")
        return None
