@echo off
REM Start FastAPI Server for AI Insurance Platform
REM This batch script starts the FastAPI development server

echo.
echo ========================================
echo   AI Insurance Platform - FastAPI Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and add it to your PATH
    pause
    exit /b 1
)

echo [INFO] Python found: 
python --version

REM Check if dependencies are installed
echo.
echo [INFO] Checking FastAPI installation...
python -c "import fastapi" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] FastAPI is not installed
    echo [INFO] Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo [INFO] All dependencies verified!
echo.
echo ========================================
echo   Starting FastAPI Server...
echo ========================================
echo.
echo Server will be available at:
echo   • Main API: http://localhost:8000
echo   • Swagger UI: http://localhost:8000/docs
echo   • ReDoc: http://localhost:8000/redoc
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

REM Start the server
uvicorn main:app --reload

pause
