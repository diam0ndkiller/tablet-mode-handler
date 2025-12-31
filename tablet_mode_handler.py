#!/bin/python3
import os
import subprocess
import sys

WORKDIR=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(WORKDIR)





APP_NAME = "Tablet Mode Handler"

OUTPUT = "eDP-1"
INPUT = "Elan Touchscreen"
TOUCHPAD = "Elan Touchpad"

LAPTOP_MODE_DPI = 86
TABLET_MODE_DPI = 96





INPUT_ROTATION_MAPPING = {
    "normal": "1 0 0  0 1 0  0 0 1",
    "left": "0 -1 1  1 0 0  0 0 1",
    "right": "0 1 0  -1 0 1  0 0 1",
    "inverted": "-1 0 1  0 -1 1  0 0 1"
}

current_mode = "laptop"



def enable_tablet_mode():
    current_mode = load_current_mode()
    if current_mode == "tablet": return
    current_mode = "tablet"
    save_current_mode(current_mode)

    toggle_touchpad(False)
    set_dpi(TABLET_MODE_DPI)
    save_panel_backup("laptop_mode")
    load_panel_backup("tablet_mode")
    send_notification("tablet", APP_NAME, "Switched to Tablet Mode")
    
def disable_tablet_mode():
    current_mode = load_current_mode()
    if current_mode == "laptop": return
    current_mode = "laptop"
    save_current_mode(current_mode)

    toggle_touchpad(True)
    set_dpi(LAPTOP_MODE_DPI)
    save_panel_backup("tablet_mode")
    load_panel_backup("laptop_mode")
    send_notification("laptopconnected", APP_NAME, "Switched to Laptop Mode")

def rotate_display(direction: str):
    rotate_xrandr_display(direction)
    remap_xinput_touchscreen(direction)



def rotate_xrandr_display(direction: str): os.system(f"xrandr --output {OUTPUT} --rotate {direction}")
def set_dpi(dpi: int): os.system(f"xfconf-query -c xsettings -p \"/Xft/DPI\" -s {dpi}")
def toggle_touchpad(state: bool): os.system(f"xinput {'enable' if state else 'disable'} \"{TOUCHPAD}\"")
def send_notification(icon: str, title: str, message: str): os.system(f"notify-send -i {icon} -t 10000 \"{title}\" \"{message}\"")
def save_panel_backup(filename: str): os.system(f"xfce4-panel-profiles save panel_backups/{filename}.panelbackup")
def load_panel_backup(filename: str): os.system(f"xfce4-panel-profiles load panel_backups/{filename}.panelbackup")

def remap_xinput_touchscreen(direction: str):
    matrix = INPUT_ROTATION_MAPPING[direction]
    os.system(f"xinput set-prop \"{INPUT}\" \"Coordinate Transformation Matrix\" {matrix}")

def load_current_mode():
    with open("current_mode.dat", "r") as file:
        mode = file.read().strip()
    if mode == "tablet": current_mode = "tablet"
    else: current_mode = "laptop"
    return current_mode

def save_current_mode(current_mode: str):
    with open("current_mode.dat", "w") as file:
        file.write(current_mode)



def main_command():
    if len(sys.argv) < 2:
        print("Please enter a command.")
        print_help()
        return

    command = sys.argv[1]

    if command in ["enable", "e", "--enable", "--e"]:
        enable_tablet_mode()
    elif command in ["disable", "d", "--disable", "--d"]:
        disable_tablet_mode()
    elif command in ["rotate", "r", "--rotate", "--r"]:
        rotate_command()
    else:
        print(f"Unknown command: {command}")

def rotate_command():
    if len(sys.argv) < 3:
        print("Please enter a direction.")
        return

    direction = sys.argv[2]

    if direction in ["normal", "left", "right", "inverted"]:
        rotate_display(direction)    
    else:
        print(f"Unknown direction: {direction}")



if __name__ == "__main__":
    main_command()















