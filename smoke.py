"""Simple smoke test for the edge detection app."""

# SPDX-License-Identifier: MIT

from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

from models.teed_model import TEEDModel
from processing.image_utils import save_edge_map


def main() -> None:
    with TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        img = np.zeros((32, 32, 3), dtype=np.uint8)
        model = TEEDModel(device="cpu")
        model.load_model()
        edges = model.process_image(img)
        save_edge_map(edges, tmp_dir / "edge.png")
        print("smoke-ok")


if __name__ == "__main__":
    main()
