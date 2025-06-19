from importlib import import_module


def test_script_importable():
    import_module("scripts.download_checkpoints")
