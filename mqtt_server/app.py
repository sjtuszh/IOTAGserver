from flask import Flask, jsonify, send_file
import io
import sqlite3
from config import DATABASE
from mqtt_client import start_mqtt_client
from database import init_db

app = Flask(__name__)

@app.route('/api/sensor_data', methods=['GET'])
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
    
    return jsonify(sensor_data)

@app.route('/api/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT image FROM images WHERE id=?', (image_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        image_data = row[0]
        return send_file(io.BytesIO(image_data), mimetype='image/jpeg')
    else:
        return 'Image not found', 404

if __name__ == '__main__':
    init_db()           # 初始化数据库
    start_mqtt_client() # 启动MQTT客户端
    app.run(host='0.0.0.0', port=5000)
