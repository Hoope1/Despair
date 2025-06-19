import numpy as np

from processing.image_utils import load_image, save_edge_map


def test_save_and_load(tmp_path):
    img = np.zeros((10, 10), dtype=np.uint8)
    output = tmp_path / "edge.png"
    save_edge_map(img, output)
    loaded = load_image(output)
    assert loaded is not None
    assert loaded.shape[0] == 10
    assert loaded.shape[1] == 10
