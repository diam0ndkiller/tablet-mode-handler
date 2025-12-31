# tablet-mode-handler
A script that handles switching to tablet mode when converting a 2-in-1 laptop.

This script watches for the laptop lid to open over 180° and switches to "Tablet Mode". In Tablet mode, a different panel layout will be applied, a higher DPI setting will be applied and the touchpad will get disabled.

> [!WARNING]
> Tested only on Lenovo IdeaPad Flex 3i CB 11igl05. For other models use `xev` to find the correct ACPI input event.

> [!NOTE]
> Uses XFCE4's DPI and Panel settings.

## Requirements
The following tools are needed in order to use this script:
- XFCE4 as a desktop (`xfce4-desktop`)
- `xfce4-panel-profiles` to load and save the panel configurations
- `acpid`

To install in Ubuntu run
```bash
sudo apt install xfce4-desktop xfce4-panel-profiles acpid
```

## Setup
Clone this repo.
### Service setup
First, edit the two files inside of `etc-acpi-events` to match the location of the script on your machine. If needed, also edit the event ID used to trigger switching. Afterwards, copy the two files into `/etc/acpi/events/`
```bash
sudo mkdir -p /etc/acpi/events
sudo cp etc-acpi-events/* /etc/acpi/events/
```

Enable `acpid`, if not done automatically by running
```bash
sudo systemctl enable acpid
```

Also make sure to open the `tablet_mode_handler_root.py` file and replace `diam0ndkiller` with your active logged in user.

### Configuration
Open the main `tablet_mode_handler.py` script and change the `OUTPUT`, `INPUT` and `TOUCHPAD` variables. You can find the needed display output by running `xrandr` and the touchscreen and touchpad inputs by running `xinput`.

If desired, change the `LAPTOP_DPI`, `TABLET_DPI` and `APP_NAME` values.

Before testing, run
```bash
xfce4-panel-profiles save panel_backups/laptop_mode.panelbackup
xfce4-panel-profiles save panel_backups/tablet_mode.panelbackup
```
to save your current panel layout configuration into BOTH the laptop and tablet mode presets.


Then, reboot your system. If everything is working, converting the laptop should trigger the script and re-load your panel. A notification confirms the script ran. Now in tablet mode you can edit your panels to make them more touch friendly, if so required. When switching back, the script will automatically save the current layout for future use in tablet mode and switch back to your previous preset.
