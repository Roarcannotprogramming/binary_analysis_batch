echo "Running test.ps1"
whoami
echo "TEST OUT" >&1
echo "TEST ERROR" >&2
echo 0 | .\ida75\idapyswitch.exe
$env:PYTHONHOME="C:\hostedtoolcache\windows\Python\3.9.13\x64"
# ls .\ida75
.\ida75\idat64.exe -B .\pwn3 2>&1 | tee .\ida.log
ls