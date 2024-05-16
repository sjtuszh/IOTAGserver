# mqtt_client.py

import paho.mqtt.client as mqtt
import json
import base64
import os
from database import insert_sensor_data, insert_image_data, insert_ec_data
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC_SENSOR, MQTT_TOPIC_IMAGE, MQTT_TOPIC_EC, IMAGES_FOLDER

def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')
    client.subscribe(MQTT_TOPIC_SENSOR)
    client.subscribe(MQTT_TOPIC_IMAGE)
    client.subscribe(MQTT_TOPIC_EC)  # 订阅新的EC数据主题

def on_message(client, userdata, msg):
    if msg.topic == MQTT_TOPIC_SENSOR:
        handle_sensor_data(msg.payload)
    elif msg.topic == MQTT_TOPIC_IMAGE:
        handle_image_data(msg.payload)
    elif msg.topic == MQTT_TOPIC_EC:
        handle_ec_data(msg.payload)  # 处理新的EC数据

def handle_sensor_data(payload):
    data = json.loads(payload)
    temperature = data.get('temperature')
    ec = data.get('ec')
    par = data.get('par')
    insert_sensor_data(temperature, ec, par)

def handle_image_data(payload):
    image_data = base64.b64decode(payload)
    image_id = int.from_bytes(image_data[:4], byteorder='big')  # assuming the first 4 bytes are a unique image id
    image_path = os.path.join(IMAGES_FOLDER, f'image_{image_id}.png')
    with open(image_path, 'wb') as image_file:
        image_file.write(image_data[4:])
    insert_image_data(image_path)

def handle_ec_data(payload):
    ec_values = json.loads(payload)
    insert_ec_data(ec_values)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt_client():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
