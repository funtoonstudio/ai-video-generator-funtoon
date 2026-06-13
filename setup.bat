@echo off
REM Test API Token and Setup

echo.
echo ========================================
echo AI Video Generator - Setup Verification
echo ========================================
echo.

if not defined REPLICATE_API_TOKEN (
    echo ❌ ERROR: REPLICATE_API_TOKEN not set!
    echo.
    echo SET YOUR TOKEN:
    echo   set REPLICATE_API_TOKEN=your_token_here
    echo.
    echo GET TOKEN FROM:
    echo   https://replicate.com/account/api-tokens
    echo.
    pause
    exit /b 1
)

echo ✅ API Token is set
echo.

echo Installing dependencies...
pip install -r requirements.txt > nul 2>&1

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

echo Testing API Token...
python test_api.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ API Token test failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ Setup Complete! Ready to run app
echo ========================================
echo.
echo Start the app with:
echo   python app.py
echo.
echo Then open:
echo   http://localhost:5000/index.html
echo.
pause
