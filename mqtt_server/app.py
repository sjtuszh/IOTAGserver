# app.py

import json
from datetime import datetime, timedelta
from flask import Flask, request, make_response, send_file, jsonify
import io
import sqlite3
from config import DATABASE, IMAGES_FOLDER
from mqtt_client import start_mqtt_client
from database import init_db
import os

# Global variable for start date
START_DATE = datetime(2024, 5, 10).date()

app = Flask(__name__)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()

    if row:
        sensor_data = {
            'id': row[0],
            'timestamp': row[1],
            'temperature': row[2],
            'ec': row[3],
            'par': row[4]
        }
        response_str = json.dumps({'data': sensor_data})
        return response_str, 200
    else:
        return 'Sensor data not found', 404

@app.route('/images', methods=['GET'])
def get_latest_image():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT image_path FROM images ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()

    if row:
        image_path = row[0]
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return 'Image not found', 404

@app.route('/ec_data', methods=['GET'])
def get_ec_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Get the current date
    current_date = datetime.now().date()

    # Calculate the difference in days
    delta_days = (current_date - START_DATE).days

    # Determine the column to retrieve based on the day
    column_index = min(delta_days // 2, 19)  # Limiting to 39 days, hence 19 columns

    # Build the SQL query
    query = f'SELECT * FROM ec_data ORDER BY id DESC LIMIT 1'
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()

    if row:
        ec_data = {
            'timestamp': row[1]
        }

        # Extracting the appropriate day's data
        ec_data[f'day_{delta_days + 1}'] = row[2 + column_index]

        response_str = json.dumps({'data': ec_data})
        return response_str, 200
    else:
        return 'EC data not found', 404

if __name__ == '__main__':
    init_db()
    start_mqtt_client()
    app.run(host='0.0.0.0', port=5000)
