import paho.mqtt.client as mqtt
import json
import random
import time

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC_EC = 'settings/ec'

def generate_ec_data():
    # 生成 20 个随机的 EC 值（0 到 5000 的整数）
    ec_values = [random.randint(0, 5000) for _ in range(20)]
    return ec_values

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    try:
        while True:
            ec_data = generate_ec_data()
            ec_payload = json.dumps(ec_data)
            client.publish(MQTT_TOPIC_EC, ec_payload)
            print(f"Published EC data: {ec_payload}")
            time.sleep(5)
    except KeyboardInterrupt:
        client.loop_stop()
        print("Simulation stopped.")

if __name__ == '__main__':
    main()

