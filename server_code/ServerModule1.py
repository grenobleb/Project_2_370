import sqlite3
from anvil.server import callable

DB_PATH = 'kanto_pokemon.db'

@callable
def get_regions():
    # Connect to the SQLite3 database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch distinct regions
    cursor.execute("SELECT DISTINCT region FROM pokemon")
    regions = [row[0] for row in cursor.fetchall()]

    conn.close()
    return regions

@callable
def get_pokemon_by_region(region):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch Pokémon names from the specified region
    cursor.execute("SELECT id, name FROM pokemon WHERE region = ?", (region,))
    pokemon_list = cursor.fetchall()

    conn.close()
    return [{'id': p[0], 'name': p[1]} for p in pokemon_list]

@callable
def get_pokemon_details(pokemon_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch Pokémon details by ID
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
            'dex_entry': result[7],
        }
    else:
        return None