from typing import Any, Optional

import numpy as np
import torch

from models.base_model import BaseEdgeDetector
from models.model_manager import ModelManager

class TEEDModel(BaseEdgeDetector):
    model_manager: ModelManager

    def __init__(self, device: str = "cuda") -> None: ...
    def load_model(self) -> None: ...
    def preprocess(self, image: np.ndarray[Any, Any]) -> torch.Tensor: ...
    def postprocess(self, output: torch.Tensor) -> np.ndarray[Any, Any]: ...
