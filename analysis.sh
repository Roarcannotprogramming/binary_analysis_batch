#!/usr/bin/env bash
# docker run --rm --env BINARY=pwn3 --name ida-docker -p 8080:8080 -v `pwd`:/root/host -it nyamisty/docker-wine-ida:7.5sp3
echo "Starting IDA..."
cp /root/host/${BINARY} /root/.wine/drive_c/
timeout 18000 wine C:\\IDA\\idat64.exe -B C:\\${BINARY}
mv /root/.wine/drive_c/${BINARY}* /root/host