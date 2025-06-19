# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
from __future__ import annotations

from abc import ABC
from typing import Any

import numpy as np
import torch

class BaseEdgeDetector(ABC):
    device: torch.device
    model: torch.nn.Module | None

    def __init__(self, device: str = "cuda") -> None: ...
    def load_model(self) -> None: ...
    def preprocess(self, image: np.ndarray[Any, Any]) -> torch.Tensor: ...
    def postprocess(self, output: torch.Tensor) -> np.ndarray[Any, Any]: ...
    def process_large_image(
        self, image: np.ndarray[Any, Any], tile_size: int = 1024, overlap: int = 128
    ) -> np.ndarray[Any, Any]: ...
    def process_image(self, image: np.ndarray[Any, Any]) -> np.ndarray[Any, Any]: ...
