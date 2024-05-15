import paho.mqtt.client as mqtt
import json
import time
import random

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC_SENSOR = 'sensor/data'

def generate_sensor_data():
    """Generate random sensor data."""
    data = {
        'temperature': random.randint(0, 40),
        'ec': random.randint(0, 5000),
        'par': random.randint(0, 3000)
    }
    return data

def publish_sensor_data(client):
    """Publish sensor data to MQTT broker."""
    while True:
        data = generate_sensor_data()
        payload = json.dumps(data)
        client.publish(MQTT_TOPIC_SENSOR, payload)
        print(f"Published data: {payload}")
        time.sleep(300)  # Wait for 5 minutes

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Start publishing sensor data
    publish_sensor_data(client)
