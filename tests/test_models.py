# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
import numpy as np
import pytest

pytest.importorskip("torch")  # noqa: E402


@pytest.fixture(autouse=True)
def no_download(monkeypatch):
    from models.model_manager import ModelManager

    monkeypatch.setattr(ModelManager, "download_dexined_weights", lambda self: None)
    monkeypatch.setattr(ModelManager, "download_teed_weights", lambda self: None)


def test_teed_model_forward():
    from models.teed_model import TEEDModel

    model = TEEDModel(device="cpu")
    model.load_model()
    img = np.zeros((32, 32, 3), dtype=np.uint8)
    edges = model.process_image(img)
    assert edges.shape == (32, 32)


def test_dexined_model_forward():
    from models.dexined_model import DexiNedModel

    model = DexiNedModel(device="cpu")
    model.load_model()
    img = np.zeros((32, 32, 3), dtype=np.uint8)
    edges = model.process_image(img)
    assert edges.shape == (32, 32)
