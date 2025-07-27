@echo off
echo Building Mahika Application (DEBUG VERSION)...
echo This version will show console output for debugging
echo.

REM Clean previous build
echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

echo.
echo Starting DEBUG build process...

REM Create a debug spec file with console enabled
(
echo # Debug build configuration
echo import os
echo.
echo block_cipher = None
echo.
echo a = Analysis^(
echo     ['main.py'],
echo     pathex=[],
echo     binaries=[],
echo     datas=[
echo         ^('src', 'src'^),
echo         ^('src/utils/audio', 'src/utils/audio'^),
echo     ],
echo     hiddenimports=[
echo         'customtkinter',
echo         'pygame',
echo         'pyttsx3',
echo         'gtts',
echo         'edge_tts',
echo         'sounddevice',
echo         'pydub',
echo         'numpy',
echo         'faster_whisper',
echo         'google.generativeai',
echo         'pymongo',
echo         'keyboard',
echo     ],
echo     hookspath=[],
echo     runtime_hooks=[],
echo     excludes=[],
echo     win_no_prefer_redirects=False,
echo     win_private_assemblies=False,
echo     cipher=block_cipher,
echo ^)
echo.
echo pyz = PYZ^(a.pure, a.zipped_data, cipher=block_cipher^)
echo.
echo exe = EXE^(
echo     pyz,
echo     a.scripts,
echo     a.binaries,
echo     a.zipfiles,
echo     a.datas,
echo     [],
echo     name='Mahika_Debug',
echo     debug=True,
echo     console=True,
echo     bootloader_ignore_signals=False,
echo     strip=False,
echo     upx=False,
echo ^)
) > debug_build.spec

REM Build with debug configuration
pyinstaller debug_build.spec

REM Check if build successful
if exist "dist\Mahika_Debug.exe" (
    echo.
    echo ========================================
    echo DEBUG BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo Debug executable created at: dist\Mahika_Debug.exe
    echo This version shows console output for troubleshooting.
    echo.
) else (
    echo.
    echo DEBUG BUILD FAILED!
    echo Check the output above for error details.
)

pause
