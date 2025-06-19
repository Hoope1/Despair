# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
from pathlib import Path
from typing import Optional

class ModelManager:
    cache_dir: Path

    def __init__(self, cache_dir: str = "checkpoints") -> None: ...
    def download_dexined_weights(self) -> Optional[str]: ...
    def download_teed_weights(self) -> Optional[str]: ...
