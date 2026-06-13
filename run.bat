@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting AI Video Generator...
echo.
echo Enter your Replicate API token when prompted
set /p REPLICATE_API_TOKEN="REPLICATE_API_TOKEN: "

set REPLICATE_API_TOKEN=%REPLICATE_API_TOKEN%
python app.py

pause
