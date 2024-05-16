# request_ec_data.py

import requests
import time

URL = 'http://localhost:5000/ec_data'

def request_ec_data():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            ec_data = response.json()
            print(f"Received EC data: {ec_data}")
        else:
            print(f"Failed to get EC data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting EC data: {e}")

def main():
    try:
        while True:
            request_ec_data()
            time.sleep(180)  # 每 3 分钟发起一次请求
    except KeyboardInterrupt:
        print("Request simulation stopped.")

if __name__ == '__main__':
    main()
