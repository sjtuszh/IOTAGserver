import cv2
import paho.mqtt.client as mqtt
import base64
import time
import os
import struct

# MQTT broker configuration
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC_IMAGE = 'sensor/image'

# Initialize MQTT client
client = mqtt.Client()

def capture_and_publish_image():
    # OpenCV to capture image from webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    ret, frame = cap.read()
    if ret:
        # Resize the frame to 640x480 pixels
        resized_frame = cv2.resize(frame, (640, 480))

        # Encode the resized frame in JPEG format
        ret, buffer = cv2.imencode('.png', resized_frame)
        if ret:
            # Create a unique ID for the image
            image_id = struct.pack('>I', int(time.time()))
            # Encode the image data to base64
            image_data = base64.b64encode(image_id + buffer.tobytes()).decode('utf-8')
            # Publish the image data to the MQTT topic
            client.publish(MQTT_TOPIC_IMAGE, image_data)
            print("Image published.")
        else:
            print("Error: Could not encode image.")
    else:
        print("Error: Could not read frame from video device.")

    cap.release()

def main():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    try:
        while True:
            capture_and_publish_image()
            time.sleep(5)  # Wait for 5 minutes before capturing the next image
    except KeyboardInterrupt:
        print("Terminating...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == '__main__':
    main()
