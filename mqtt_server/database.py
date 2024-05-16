# database.py

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
            image_path TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ec_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            day_1 INTEGER,
            day_3 INTEGER,
            day_5 INTEGER,
            day_7 INTEGER,
            day_9 INTEGER,
            day_11 INTEGER,
            day_13 INTEGER,
            day_15 INTEGER,
            day_17 INTEGER,
            day_19 INTEGER,
            day_21 INTEGER,
            day_23 INTEGER,
            day_25 INTEGER,
            day_27 INTEGER,
            day_29 INTEGER,
            day_31 INTEGER,
            day_33 INTEGER,
            day_35 INTEGER,
            day_37 INTEGER,
            day_39 INTEGER
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

def insert_image_data(image_path):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images (image_path) VALUES (?)
    ''', (image_path,))
    conn.commit()
    conn.close()

def insert_ec_data(ec_values):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ec_data (day_1, day_3, day_5, day_7, day_9, day_11, day_13, day_15, day_17, day_19, day_21, day_23, day_25, day_27, day_29, day_31, day_33, day_35, day_37, day_39)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', ec_values)
    conn.commit()
    conn.close()
