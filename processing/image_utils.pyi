# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
from pathlib import Path
from typing import Any, Optional, Tuple

import numpy as np

def load_image(image_path: str | Path) -> Optional[np.ndarray[Any, Any]]: ...
def save_edge_map(
    edge_map: np.ndarray[Any, Any],
    output_path: str | Path,
    original_size: Optional[Tuple[int, int]] = None,
) -> None: ...
