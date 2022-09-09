#!/usr/bin/env bash
# docker run --rm --env BINARY=pwn3 --name ida-docker -p 8080:8080 -v `pwd`:/root/host -it nyamisty/docker-wine-ida:7.5sp3
echo "Starting IDA..."
cp /root/host/* /root/.wine/drive_c/
find /root/host -type f | xargs cp - /root/.wine/drive_c/
ls -alh /root/.wine/drive_c
# cp /root/host/analysis.py /root/.wine/drive_c/
rm /root/.wine/drive_c/IDA/plugins/ipyida_plugin_stub.py
wine C:\\IDA\\idat64.exe -L"C:\\ida_log" -A -S"C:\\analysis.py" C:\\${BINARY}
mv /root/.wine/drive_c/${BINARY}* /root/host
mv /root/.wine/drive_c/ida_log /root/host
echo "Done"