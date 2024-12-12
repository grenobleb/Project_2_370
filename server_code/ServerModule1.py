import sqlite3
from anvil.server import callable

DB_PATH = 'kanto_pokemon.db'

@callable
def get_regions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT region FROM pokemon")
    regions = [row[0] for row in cursor.fetchall()]
    conn.close()
    return regions

@callable
def get_pokemon_by_region(region):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM pokemon WHERE region = ?", (region,))
    result = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    conn.close()
    return result

@callable
def get_pokemon_details(pokemon_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE id = ?", (pokemon_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            'id': result[0],
            'name': result[1],
            'region': result[2],
            'category': result[3],
            'type': result[4],
            'avg_weight': result[5],
            'avg_height': result[6],
            'dex_entry': result[7]
        }
    else:
        return None