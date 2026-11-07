param([Parameter(Mandatory)][string]$RuntimeDirectory)
$ErrorActionPreference = 'Stop'
$destination = Join-Path $PSScriptRoot 'dist'
New-Item -ItemType Directory -Force (Join-Path $destination 'runtime') | Out-Null
$extractor = Join-Path (Split-Path -Parent $PSScriptRoot) 'extract_nms_bases.py'
$source = [Convert]::ToBase64String([IO.File]::ReadAllBytes($extractor))
$template = Get-Content -Raw -Encoding UTF8 (Join-Path $PSScriptRoot 'index.template.html')
$template.Replace('__EXTRACTOR_BASE64__', $source) |
    Set-Content -Encoding UTF8 (Join-Path $destination 'index.html')
foreach ($file in 'pyodide.js', 'pyodide.asm.js', 'pyodide.asm.wasm', 'python_stdlib.zip', 'pyodide-lock.json', 'PYODIDE-LICENSE.txt') {
    Copy-Item -LiteralPath (Join-Path $RuntimeDirectory $file) -Destination (Join-Path $destination 'runtime')
}
foreach ($file in 'serve.ps1', 'Start Base Reports.cmd') {
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot $file) -Destination $destination
}
