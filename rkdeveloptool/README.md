# rkdeveloptool

Command-line tool for flashing Rockchip devices via USB (Maskrom/Loader mode).

## Usage

```bash
# List connected devices
rkdeveloptool ld

# Download loader (enter loader mode from maskrom)
rkdeveloptool db rv1106_download_v1.15.108.bin

# Write partition
rkdeveloptool wl 0x40 idblock.img

# Reset device
rkdeveloptool rd
```

## Build Dependencies

- libusb-1.0-dev
- libudev-dev
- cmake

## udev Rules

To use without root, install udev rules:

```bash
sudo cp 99-rk-rockusb.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
```
