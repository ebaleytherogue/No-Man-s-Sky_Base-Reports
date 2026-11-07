# NMS Base Reports for Windows

Select an exported No Man's Sky save JSON and a destination folder, then click **Generate Reports**. The application writes `nms_bases_master.csv` and `nms_bases_summary.md`. Existing reports with those names are replaced, and the extractor removes its two obsolete report files as before. Choose a fresh output folder to keep previous reports.

## Run or build from source

Use Windows Python with Tcl/Tk installed. In PowerShell, from this folder, run:

    python -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements-windows.txt
    .\.venv\Scripts\python.exe base_reports_gui.py
    .\build-windows.ps1 -Python .\.venv\Scripts\python.exe

Distribute the entire `dist\NMS Base Reports` folder as a ZIP. Extract it and double-click `NMS Base Reports.exe`. Keep the supporting files beside the executable. The build collects CustomTkinter's themes and fonts.

The existing command-line interface is available through `extract_nms_bases.py` with the same arguments.
