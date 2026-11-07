param([string]$Python = "python")
$ErrorActionPreference = "Stop"

Push-Location $PSScriptRoot
try {
    & $Python -m PyInstaller --noconfirm --onedir --windowed --collect-data customtkinter --name "NMS Base Reports" --specpath build base_reports_gui.py
    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller failed with exit code $LASTEXITCODE."
    }
} finally {
    Pop-Location
}
