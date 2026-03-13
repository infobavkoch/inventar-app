import sqlite3

conn = sqlite3.connect("data/database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fahrzeuge (
id INTEGER PRIMARY KEY AUTOINCREMENT,
bezeichnung TEXT,
kennzeichen TEXT,
funkrufname TEXT,
tuev TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS feuerloescher (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fahrzeug_id INTEGER,
nummer TEXT,
pruefung TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sauerstoff (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fahrzeug_id INTEGER,
nummer TEXT,
pruefung TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS wartung (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fahrzeug_id INTEGER,
datum TEXT,
notizen TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS elektrisch (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fahrzeug_id INTEGER,
datum TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS meetb (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fahrzeug_id INTEGER,
name TEXT,
nummer TEXT,
pruefung TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tragelagerung (
id INTEGER PRIMARY KEY AUTOINCREMENT,
bezeichnung TEXT,
sicht TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS beleuchtung (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
pruefung TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fi_check (
id INTEGER PRIMARY KEY AUTOINCREMENT,
bezeichnung TEXT,
datum TEXT
)
""")

conn.commit()
