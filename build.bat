@echo off
echo Building Mahika Application...
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)

REM Clean previous build
echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.spec" del "*.spec"

echo.
echo Starting build process...
echo This may take several minutes...

REM Build with PyInstaller using the spec file
pyinstaller build_config.spec

REM Check if build successful
if exist "dist\Mahika.exe" (
    echo.
    echo ========================================
    echo BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo Executable created at: dist\Mahika.exe
    echo File size: 
    for %%A in ("dist\Mahika.exe") do echo %%~zA bytes
    echo.
    echo The entire 'dist' folder can be distributed to users.
    echo Users do NOT need Python installed to run this application.
    echo.
    echo Testing the executable...
    echo Press Ctrl+C to stop the test if needed.
    timeout /t 3 /nobreak >nul
    start "" "dist\Mahika.exe"
    echo.
    echo If the application started successfully, the build is complete!
    echo You can now share the 'dist' folder with users.
    echo.
) else (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    echo.
    echo Please check the errors above.
    echo Common issues:
    echo - Missing dependencies
    echo - Import errors
    echo - Path issues
    echo.
    echo Try running with console mode for debugging:
    echo pyinstaller --console build_config.spec
)

echo.
pause
