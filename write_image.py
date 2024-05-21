import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
import time

def capture_and_save_image():
    try:
        # Replace with your MJPG-Streamer's URL
        stream_url = "http://172.23.52.167:8080/?action=snapshot"

        # Fetch the image from the stream
        response = requests.get(stream_url)
        if response.status_code == 200:
            # Convert the response content to an image
            image = Image.open(BytesIO(response.content))
            
            # Generate filename with timestamp
            filename = datetime.now().strftime("./save_images/captured_image_%Y%m%d_%H%M%S.jpg")

            # Save the image
            image.save(filename)
            print(f"Image captured and saved as '{filename}'")
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    while True:
        capture_and_save_image()
        # Sleep for 30 minutes
        time.sleep(30 * 60)
