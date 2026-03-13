import sqlite3

def get_connection():
    conn = sqlite3.connect("inventar.db", check_same_thread=False)
    return conn

def init_db():

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS fahrzeuge(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bezeichnung TEXT,
    kennzeichen TEXT,
    funkrufname TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS tuev(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fahrzeug_id INTEGER,
    termin TEXT
    )
    """)

    conn.commit()
