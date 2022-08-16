echo "Running test.ps1"
echo 0 | .\ida75\idapyswitch.exe
$env:PYTHONHOME="C:\hostedtoolcache\windows\Python\3.9.13\x64"
New-ItemProperty -Path 'HKCU:\SOFTWARE\Hex-Rays\IDA' -Name 'License Hex-Rays SA. 銆愯珛鏀寔姝ｇ増銆? Unlimited License' -Value "1" -PropertyType DWORD -Force
# Set-NetFirewallProfile -Profile Private -Enabled False
# Set-NetFirewallProfile -Profile Public -Enabled False
# ls .\ida75
.\ida75\idat64.exe -B .\pwn3 2>&1 | tee .\ida.log
ls