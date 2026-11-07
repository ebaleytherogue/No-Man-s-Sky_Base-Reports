param([switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$files = @{
    '/' = @('index.html', 'text/html; charset=utf-8')
    '/runtime/pyodide.js' = @('runtime/pyodide.js', 'text/javascript')
    '/runtime/pyodide.asm.js' = @('runtime/pyodide.asm.js', 'text/javascript')
    '/runtime/pyodide.asm.wasm' = @('runtime/pyodide.asm.wasm', 'application/wasm')
    '/runtime/python_stdlib.zip' = @('runtime/python_stdlib.zip', 'application/zip')
    '/runtime/pyodide-lock.json' = @('runtime/pyodide-lock.json', 'application/json')
}
$server = [Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback, 0)
$server.Start()
try {
    $url = "http://127.0.0.1:$($server.LocalEndpoint.Port)/"
    Write-Host "Base Reports is running at $url"
    Write-Host 'Keep this window open while using the app. Close it when finished.'
    if (-not $NoBrowser) {
        $chrome = @(
            "$env:ProgramFiles\Google\Chrome\Application\chrome.exe"
            "$([Environment]::GetEnvironmentVariable('ProgramFiles(x86)'))\Google\Chrome\Application\chrome.exe"
            "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
        ) | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
        if ($chrome) { Start-Process -FilePath $chrome -ArgumentList $url }
        else { Start-Process $url }
    }
    while ($true) {
        $client = $server.AcceptTcpClient()
        try {
            $client.ReceiveTimeout = 2000
            $client.SendTimeout = 10000
            $stream = $client.GetStream()
            $reader = [IO.StreamReader]::new($stream)
            $request = $reader.ReadLine()
            if ($request -match '^GET (/[^ ?]*)(?:\?[^ ]*)? HTTP/1\.[01]$' -and $files.ContainsKey($Matches[1])) {
                $file, $type = $files[$Matches[1]]
                $body = [IO.File]::ReadAllBytes((Join-Path $PSScriptRoot $file))
                $status = '200 OK'
            } else {
                $body = [byte[]]@()
                $type = 'text/plain'
                $status = '404 Not Found'
            }
            $header = [Text.Encoding]::ASCII.GetBytes("HTTP/1.1 $status"+[char]13+[char]10+"Content-Type: $type"+[char]13+[char]10+"Content-Length: $($body.Length)"+[char]13+[char]10+"Connection: close"+[char]13+[char]10+[char]13+[char]10)
            $stream.Write($header, 0, $header.Length)
            $stream.Write($body, 0, $body.Length)
        } catch [IO.IOException] {
            # A browser may close an unused connection.
        } finally {
            $client.Dispose()
        }
    }
} finally {
    $server.Stop()
}
