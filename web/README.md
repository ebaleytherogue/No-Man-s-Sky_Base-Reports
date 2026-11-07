# Base Reports browser app

The Windows offline build uses the same extractor as the desktop tool. The build embeds the repository-root extractor in the browser page. The Windows launcher serves the bundled files on the local computer, and the browser processes the save.

## Build

Supply a directory containing the Pyodide 0.27.7 core runtime files and the upstream license saved as PYODIDE-LICENSE.txt. From the repository root run:

    pwsh -NoProfile -File web/build.ps1 -RuntimeDirectory PATH_TO_RUNTIME

Open Start Base Reports.cmd in web/dist. The generated dist folder is ignored by Git.

## Verify

Select fixtures/synthetic-save.json and generate both reports. Compare the CSV byte for byte against fixtures/expected. Normalize CRLF and LF before comparing Markdown. Use fictional saves for committed test fixtures.
