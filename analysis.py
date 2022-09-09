#!/usr/bin/env python3

import threading
import ida_kernwin
import ida_auto
import ida_pro
import time


def timout_thread_func():
    print("Timeout thread started")
    time.sleep(int(5.5*60*60))
    print("Now! Analysis Timeout!")
    c = compile('ida_pro.qexit(0)', '', 'exec')
    ida_kernwin.execute_sync(lambda: exec(c), ida_kernwin.MFF_WRITE)

t = threading.Thread(target=timout_thread_func)
t.daemon = True
t.start()

print("Main thread started")