#!/bin/bash

#!/bin/bash

# Path to mjpg_streamer directory
MJPG_STREAMER_PATH="/home/pi2w/mjpg-streamer/mjpg-streamer-experimental"

# Start mjpg_streamer
$MJPG_STREAMER_PATH/mjpg_streamer -i "$MJPG_STREAMER_PATH/input_uvc.so -d /dev/video0 -r 640x480 -f 30" -o "$MJPG_STREAMER_PATH/output_http.so -w $MJPG_STREAMER_PATH/www"
