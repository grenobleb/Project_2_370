import sqlite3
from anvil.server import callable

DB_PATH = 'kanto_pokemon.db'

@callable
def check_table_exists():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pokemon';")
    table = cursor.fetchone()
    conn.close()
    return table is not None