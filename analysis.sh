#!/usr/bin/env bash
# docker run --rm --env BINARY=pwn3 --name ida-docker -p 8080:8080 -v `pwd`:/root/host -it nyamisty/docker-wine-ida:7.5sp3

# watch_file() {
#     while true; do
#         if [ "$(cat /root/.wine/drive_c/ida_log | grep "The initial autoanalysis has been finished.")" ]; then
#             echo "[+] Already completed! Exit"
#             kill -s SIGTERM $$
#             exit 0
#         fi
#         sleep 60
#     done
# }

do_save() {
    echo "[+] Print Ida Log"
    cat /root/.wine/drive_c/ida_log
    echo "[*] Save"
    mv /root/.wine/drive_c/${BINARY}* /root/host
    mv /root/.wine/drive_c/ida_log /root/host
    echo "[+] Save Done"
}

# trap "do_save; exit 0" SIGINT SIGTERM

echo "Starting IDA..."
echo ${BINARY}
# cp /root/host/* /root/.wine/drive_c/
# find /root/host -type f | xargs cp /root/.wine/drive_c/
for f in $(find /root/host -type f -maxdepth 1); do
    cp $f /root/.wine/drive_c/
done
ls -alh /root/.wine/drive_c
# watch_file &
rm /root/.wine/drive_c/IDA/plugins/ipyida_plugin_stub.py
wine C:\\IDA\\idat64.exe -L"C:\\ida_log" -A -S"C:\\analysis.py" C:\\${BINARY}
do_save