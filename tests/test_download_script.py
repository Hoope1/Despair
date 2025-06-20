# SPDX-FileCopyrightText: 2025 The Despair Authors
# SPDX-License-Identifier: MIT
from importlib import import_module


def test_script_importable():
    import_module("scripts.download_weights")
