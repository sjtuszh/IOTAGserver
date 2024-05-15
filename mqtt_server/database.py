import sqlite3
from config import DATABASE

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature INTEGER,
            ec INTEGER,
            par INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            image BLOB
        )
    ''')
    conn.commit()
    conn.close()

def insert_sensor_data(temperature, ec, par):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (temperature, ec, par) VALUES (?, ?, ?)
    ''', (temperature, ec, par))
    conn.commit()
    conn.close()

def insert_image_data(image_data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images (image) VALUES (?)
    ''', (image_data,))
    conn.commit()
    conn.close()
