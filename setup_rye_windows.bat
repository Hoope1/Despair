REM SPDX-FileCopyrightText: 2025 The Despair Authors
REM SPDX-License-Identifier: MIT
@echo off
echo ========================================
echo Edge Detection App - Rye Setup (Windows)
echo ========================================
echo.

REM Check if Rye is installed
where rye >nul 2>&1
if %errorlevel% neq 0 (
    echo Rye is not installed. Installing Rye...
    echo.

    REM Download and install Rye
    echo Downloading Rye installer...
    curl -sSf https://rye.astral.sh/get -o rye-installer.py

    echo Installing Rye...
    python rye-installer.py

    REM Add Rye to PATH
    set "PATH=%USERPROFILE%\.rye\shims;%PATH%"

    echo.
    echo Rye installed successfully!
    echo Please restart your terminal after installation completes.
    echo.

    del rye-installer.py
) else (
    echo Rye is already installed.
)

echo.
echo ========================================
echo Setting up Edge Detection project...
echo ========================================
echo.

REM Initialize Rye project
echo Initializing Rye project...
rye init --no-readme --no-license --no-pin --python 3.10

REM Sync dependencies
echo.
echo Installing dependencies...
rye sync

REM Fix PyQt6 DLL issues on Windows
echo.
echo Fixing PyQt6 installation...
rye run pip uninstall -y PyQt6 PyQt6-Qt6 PyQt6-sip
rye run pip install --force-reinstall --no-cache-dir PyQt6==6.9.1 PyQt6-Qt6==6.9.1 PyQt6_sip==13.10.2

REM Install PyTorch with CUDA support
echo.
echo Installing PyTorch with CUDA support...
rye run pip install torch==2.1.0+cu118 torchvision==0.16.0+cu118 --index-url https://download.pytorch.org/whl/cu118

REM Download model weights
echo.
echo Downloading model weights...
rye run python scripts/download_weights.py

echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To run the application:
echo   rye run python main.py
echo.
echo Or activate the virtual environment:
echo   .venv\Scripts\activate
echo   python main.py
echo.

pause
