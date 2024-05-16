# stream-image-pizero

## Raspberry Pi Zero 2

1. Install Dependencies 
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