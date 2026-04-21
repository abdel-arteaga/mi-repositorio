import sqlite3

DB_NAME = "biblioteca.db"

def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with conectar() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            estado TEXT NOT NULL CHECK(estado IN ('Leído','No leído'))
        );
        """)