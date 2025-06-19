# SPDX-License-Identifier: MIT

import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from gui.main_window import EdgeDetectionApp


def main():
    # Create necessary directories
    Path("checkpoints").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)
    Path("output/TEED").mkdir(parents=True, exist_ok=True)
    Path("output/DexiNed").mkdir(parents=True, exist_ok=True)

    # Check CUDA availability
    import torch

    if torch.cuda.is_available():
        print(f"CUDA available: {torch.cuda.get_device_name(0)}")
        print(f"CUDA version: {torch.version.cuda}")
    else:
        print("WARNING: CUDA not available, using CPU (will be slower)")

    # Start GUI application
    app = QApplication(sys.argv)
    window = EdgeDetectionApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
