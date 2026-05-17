@echo off
rem Windows cmd wrapper cho zero_write
chcp 65001 >nul
setlocal
set "SCRIPT=%~dp0main.py"
set "PYTHONIOENCODING=utf-8"
if "%~1"=="" (
  echo Usage: zw [text] {hidden}
  echo.
  echo   zw "Tôi [yêu] em"
  echo   zw "Tôi [___] em" "yêu"
  echo   zw reveal "Tôi [yêu] em"
  echo   zw merge "Tôi [___] em" "yêu"
  exit /b 1
)
python "%SCRIPT%" %*
