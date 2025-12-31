#!/bin/python3
import os
import sys


# CALLED FROM
# /etc/acpi/events/tablet-mode
# /etc/acpi/events/laptop-mode


WORKDIR=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(WORKDIR)

EXECUTABLE = "tablet_mode_handler.py"

command = f"sudo -u diam0ndkiller DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus {WORKDIR}/{EXECUTABLE}"

for i, parameter in enumerate(sys.argv):
    if i == 0: continue
    command += f" {parameter}"

os.system(command)
