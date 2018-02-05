#!/usr/bin/python

import time
import fcntl
import os
import signal

command = ""


FNAME = "/home/ec2-user/uploads/"

def handler(signum, frame):
    print "Files modified, sending notification"
    os.system(command)
signal.signal(signal.SIGIO, handler)
fd = os.open(FNAME,  os.O_RDONLY)
fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
fcntl.fcntl(fd, fcntl.F_NOTIFY,
            fcntl.DN_MODIFY | fcntl.DN_CREATE | fcntl.DN_MULTISHOT)

while True:
    time.sleep(10000)