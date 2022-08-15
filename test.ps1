echo "Running test.ps1"
echo 0 | .\ida75\idapyswitch.exe
$env:PYTHONHOME="C:\hostedtoolcache\windows\Python\3.9.13\x64"
Get-ChildItem env:
.\ida75\idat64.exe -B .\pwn3 2>&1
ls