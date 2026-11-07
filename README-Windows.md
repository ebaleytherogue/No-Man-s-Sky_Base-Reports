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

## GitHub releases

After this workflow is on GitHub, publish a release using a tag that includes it.
The Windows portable build workflow checks the synthetic save reports and builds
the x64 ZIP from that release commit. When it succeeds,
`NMS-Base-Reports-Windows-x64-Portable.zip` appears under the release's Assets.

To try the build before publishing, open **Actions → Windows portable build →
Run workflow** and select the branch to build. Download the ZIP from the run's
Artifacts. A manual run leaves release assets untouched.
