chcp 65001 > nul
REM This script updates the MITRE ATT&CK data repository by pulling the latest changes from the remote repository.
@echo off
setlocal

:: --- Set Variables ---
set "REPO_DIR=C:\Users\ayujo\SPRING 2025\IST 402\NVD&MTK\attack-stix-data"
set "LOG_FILE=C:\Users\ayujo\SPRING 2025\IST 402\NVD&MTK\MITRE_update_log.txt"
set "ERROR_LOG=C:\Users\ayujo\SPRING 2025\IST 402\NVD&MTK\MITRE_error_log.txt"

:: --- Timestamp ---
set "DATETIME=%date% %time%"

:: --- Echo start ---
echo =============================
echo "🛠 Updating MITRE ATT&CK Data"
echo =============================
echo.

:: --- Navigate to repo ---
cd /d "%REPO_DIR%"

:: --- Run git pull and log output ---
echo [%DATETIME%] Starting update >> "%LOG_FILE%"
git pull >> "%LOG_FILE%" 2>> "%ERROR_LOG%"

:: --- Check if success ---
IF %ERRORLEVEL% EQU 0 (
    echo [%DATETIME%] ✅ Update successful! >> "%LOG_FILE%"
    echo ✅ Update successful!
) ELSE (
    echo [%DATETIME%] ❌ Update failed! See error_log.txt >> "%LOG_FILE%"
    echo ❌ Update failed! Check error_log.txt for details.
)

:: --- Done ---
endlocal
pause
