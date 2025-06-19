# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
"""Simple smoke test for the edge detection models."""
from __future__ import annotations

import numpy as np

from models.dexined_model import DexiNedModel
from models.teed_model import TEEDModel


def main() -> None:
    """Run a minimal inference to verify models execute."""
    image = np.zeros((32, 32, 3), dtype=np.uint8)

    teed = TEEDModel(device="cpu")
    teed.load_model()
    _ = teed.process_image(image)

    dexined = DexiNedModel(device="cpu")
    dexined.load_model()
    _ = dexined.process_image(image)


if __name__ == "__main__":
    main()
