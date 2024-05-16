from flask import Flask, request, make_response, send_file
import io
import sqlite3
from config import DATABASE, IMAGES_FOLDER
from mqtt_client import start_mqtt_client
from database import init_db
import os

app = Flask(__name__)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()

    sensor_data = []
    for row in rows:
        sensor_data.append({
            'id': row[0],
            'timestamp': row[1],
            'temperature': row[2],
            'ec': row[3],
            'par': row[4]
        })

    response = make_response({'data': sensor_data})
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT image_path FROM images WHERE id=?', (image_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        image_path = row[0]
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return 'Image not found', 404

if __name__ == '__main__':
    init_db()  # 初始化数据库
    start_mqtt_client()  # 启动MQTT客户端
    app.run(host='0.0.0.0', port=5000)
