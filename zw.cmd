@echo off
rem Windows cmd wrapper cho zero_write
chcp 65001 >nul
setlocal
set "SCRIPT=%~dp0main.py"
set "PYTHONIOENCODING=utf-8"
if "%~1"=="" (
  echo Usage: zw [text] {hidden}
  echo.
  echo   zw "Tôi [và] bạn"
  echo   zw "Tôi [___] bạn" "và"
  echo   zw reveal "Tôi [với] bạn "
  echo   zw merge "Tôi [___] bạn" "với"
  exit /b 1
)
python "%SCRIPT%" %*
