@echo off
echo ========================================
echo Edge Detection App - Conda Setup
echo ========================================
echo.
echo This is an alternative setup using Conda/Miniconda
echo which often works better with PyQt6 on Windows.
echo.

REM Check if conda is available
where conda >nul 2>&1
if %errorlevel% neq 0 (
    echo Conda not found!
    echo Please install Miniconda from: https://docs.conda.io/en/latest/miniconda.html
    echo.
    pause
    exit /b 1
)

echo Found Conda installation.
echo.

REM Remove existing environment if it exists
echo Checking for existing environment...
conda env list | findstr /C:"edge_detection" >nul 2>&1
if %errorlevel% equ 0 (
    echo Removing existing edge_detection environment...
    conda env remove -n edge_detection -y
)

REM Create new environment with Python 3.10
echo Creating new conda environment with Python 3.10...
conda create -n edge_detection python=3.10 -y

REM Activate environment
echo.
echo Activating environment...
call conda activate edge_detection

REM Install PyQt6 from conda-forge (more reliable on Windows)
echo.
echo Installing PyQt6 from conda-forge...
conda install -c conda-forge pyqt -y

REM Install PyTorch with CUDA
echo.
echo Installing PyTorch with CUDA support...
conda install pytorch==2.1.0 torchvision==0.16.0 pytorch-cuda=11.8 -c pytorch -c nvidia -y

REM Install other dependencies with pip
echo.
echo Installing remaining dependencies...
pip install opencv-python==4.8.1.78 numpy==1.24.3 Pillow==10.1.0
pip install matplotlib==3.7.2 h5py==3.10.0 scipy==1.11.4
pip install kornia==0.7.0 tqdm==4.66.1
pip install gdown==4.7.1 requests==2.31.0

REM Download model weights
echo.
echo Downloading model weights...
python scripts/download_weights.py

REM Create launch script for conda
echo @echo off > launch_edge_detection_conda.bat
echo echo Starting Edge Detection Application... >> launch_edge_detection_conda.bat
echo call conda activate edge_detection >> launch_edge_detection_conda.bat
echo python main.py >> launch_edge_detection_conda.bat
echo if %%errorlevel%% neq 0 pause >> launch_edge_detection_conda.bat

echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To run the application:
echo   launch_edge_detection_conda.bat
echo.
echo Or manually:
echo   conda activate edge_detection
echo   python main.py
echo.

pause
