echo "Running test.ps1"
echo 0 | .\ida75\idapyswitch.exe
.\ida75\idat64.exe -B .\pwn3
ls