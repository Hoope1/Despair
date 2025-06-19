from typing import Dict

from PyQt6.QtCore import QThread, pyqtSignal

class BatchProcessor(QThread):
    progress_update: pyqtSignal
    log_message: pyqtSignal
    processing_complete: pyqtSignal
    current_file_update: pyqtSignal
    folder_path: str
    models: Dict[str, object]

    def __init__(self, folder_path: str) -> None: ...
    def run(self) -> None: ...
    def _initialize_models(self) -> None: ...
    def _get_image_files(self) -> list[str]: ...
