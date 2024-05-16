# stream-image-pizero

## Raspberry Pi Zero 2

1. Install Dependencies, if dependencies are installed, skip this part to 6.
```bash
sudo apt update
sudo apt install build-essential libjpeg8-dev imagemagick libv4l-dev cmake git
```

2. Clone MJPG-streamer
```bash
git clone https://github.com/jacksonliam/mjpg-streamer.git
```

3. Build MJPG-streamer
```bash
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
```

4. Optional, confirm connection of USB camera
```bash
ls /dev/video*
```

5. Start MJPG-streamer
```bash
./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -r 640x480 -f 30" -o "./output_http.so -w ./www"
```

### Run on startup
Start stream
```bash
cp ./start_mjpg_streamer.sh /usr/local/bin/start_mjpg_streamer.sh
sudo chmod +x /usr/local/bin/start_mjpg_streamer.sh
```

### Troubleshooting
- Check udev Logs:
If the script doesn't run as expected, check the udev logs for errors:
```bash
sudo journalctl -u systemd-udevd
```
- Verify Permissions: Ensure the script and MJPG-Streamer have the necessary permissions. Running the script manually should help verify this:
```bash
sudo /usr/local/bin/start_mjpg_streamer.sh
```
Debug udev Rules: Use udevadm to test if the rules are being triggered correctly:
```bash
sudo udevadm test /dev/video0
```

Run on startup
```bash
sudo nano /etc/udev/rules.d/99-usb-camera.rules ## add following content SUBSYSTEM=="video4linux", KERNEL=="video[0-9]*", ACTION=="add", RUN+="/usr/local/bin/start_mjpg_streamer.sh"

# Reload udev and apply changes
sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Client

Access the stream via HTTP

Stream
```
http://<RaspberryPiIPAddress>:8080/?action=stream
```

Snapshot
```
http://<RaspberryPiIPAddress>:8080/?action=snapshot
```

## Run client application
Stream
```
http://<RaspberryPiIPAddress>:8080
```