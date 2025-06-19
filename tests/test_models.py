# SPDX-License-Identifier: MIT

import numpy as np
import pytest

from models.dexined_model import DexiNedModel
from models.model_manager import ModelManager
from models.teed_model import TEEDModel


@pytest.fixture(autouse=True)
def no_download(monkeypatch):
    monkeypatch.setattr(ModelManager, "download_dexined_weights", lambda self: None)
    monkeypatch.setattr(ModelManager, "download_teed_weights", lambda self: None)


def test_teed_model_forward():
    model = TEEDModel(device="cpu")
    model.load_model()
    img = np.zeros((32, 32, 3), dtype=np.uint8)
    edges = model.process_image(img)
    assert edges.shape == (32, 32)


def test_dexined_model_forward():
    model = DexiNedModel(device="cpu")
    model.load_model()
    img = np.zeros((32, 32, 3), dtype=np.uint8)
    edges = model.process_image(img)
    assert edges.shape == (32, 32)
