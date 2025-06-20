# Edge Detection App - Windows Installation Guide

## Prerequisites

1. **Python 3.10 or 3.11** (NOT 3.12 - PyQt6 compatibility issues)
   - Download from: https://www.python.org/downloads/
   - ✅ Check "Add Python to PATH" during installation

2. **Microsoft Visual C++ Redistributables**
   - Required for PyQt6
   - Download: https://aka.ms/vs/17/release/vc_redist.x64.exe
   - Install and restart if needed

3. **NVIDIA GPU Driver** (optional, for GPU acceleration)
   - Download from: https://www.nvidia.com/drivers

## Installation Methods

### Method 1: Automatic Setup with Rye (Recommended)

1. **Run the setup script:**
   ```batch
   setup_rye_windows.bat
   ```
   This will:
   - Install Rye (modern Python package manager)
   - Create virtual environment
   - Install all dependencies
   - Fix PyQt6 DLL issues
   - Download model weights

2. **Launch the application:**
   ```batch
   launch_edge_detection_rye.bat
   ```

### Method 2: Manual Rye Installation

1. **Install Rye:**
   ```powershell
   # In PowerShell (as Administrator)
   irm https://rye.astral.sh/get | iex
   ```

2. **Clone and setup project:**
   ```batch
   cd edge-detection-app
   rye sync
   ```

3. **Fix PyQt6 (if needed):**
   ```batch
   rye run python fix_pyqt6_dll.py
   ```

4. **Run application:**
   ```batch
   rye run python main.py
   ```

### Method 3: Traditional pip Installation

1. **Create virtual environment:**
   ```batch
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```batch
   pip install -r requirements.txt
   ```

3. **Fix PyQt6 DLL issues:**
   ```batch
   python fix_pyqt6_dll.py
   ```

4. **Download model weights:**
   ```batch
   python scripts/download_weights.py
   ```

5. **Run application:**
   ```batch
   python main.py
   ```

## Troubleshooting

### PyQt6 DLL Error
```plaintext
ImportError: DLL load failed while importing QtCore
```

**Solutions:**
1. Install Visual C++ Redistributables (link above)
2. Run `fix_pyqt6_dll.py`
3. Use Python 3.10 or 3.11 (not 3.12)
4. Try Anaconda instead:
   ```batch
   conda install -c conda-forge pyqt
   ```

## Verifying Installation

Run the verification script:
```batch
rye run python verify_installation.py
```
