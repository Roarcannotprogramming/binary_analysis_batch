#!/usr/bin/env python3

from re import T
import threading
import ida_kernwin
import ida_auto
import ida_pro
import time


def timout_thread_func():
    print("[*] Timeout thread started")
    # time.sleep(int(5.5*60*60))
    for i in range(0, 5*60):
        print("[*] Passed {} seconds".format(i))
        time.sleep(1)
    print("[+] Now! Analysis Timeout!")
    c = compile('ida_pro.qexit(0)', '', 'exec')
    ida_kernwin.execute_sync(lambda: exec(c), ida_kernwin.MFF_WRITE)

def auto_ok_thread_func():
    print("[*] Auto OK thread started")
    while True:
        if ida_kernwin.execute_sync(lambda: ida_auto.auto_is_ok(), ida_kernwin.MFF_WRITE):
            print("[+] Auto analysis OK! Exit")
            break
        time.sleep(5)
    c = compile('ida_pro.qexit(0)', '', 'exec')
    ida_kernwin.execute_sync(lambda: exec(c), ida_kernwin.MFF_WRITE)

timout_thread = threading.Thread(target=timout_thread_func)
auto_ok_thread = threading.Thread(target=auto_ok_thread_func)
timout_thread.daemon = True
auto_ok_thread.daemon = True
timout_thread.start()
auto_ok_thread.start()

print("[*] Analysis begin...")