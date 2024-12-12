import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def get_regions():
    # Query the table and collect unique regions
    regions = set(row['region'] for row in app_tables.pokemon.search())
    return sorted(regions)  # Return sorted regions for consistent ordering

# Function to fetch Pokémon by region
@anvil.server.callable
def get_pokemon_by_region(region):
  try:
    # Query all Pokémon that match the selected region
    rows = app_tables.pokemon.search(region=region)
        
    # Return Pokémon names for the dropdown, and their IDs to fetch full data later
    pokemon_list = [(row['name'], row['id']) for row in rows]  # Name and ID
    return pokemon_list
  except Exception as e:
    return f"Error fetching Pokémon for region {region}: {e}"

# Function to fetch Pokémon data by name
@anvil.server.callable
def get_pokemon_by_name(name):
  try:
    # Search for a Pokémon by its name
    row = app_tables.pokemon.get(name=name)
    if row:
      # Return Pokémon details including ID
      return {
        'id': row['id'],
        'name': row['name'],
        'region': row['region'],
        'category': row['category'],
        'type': row['type'],
        'avg_weight': row['avg_weight'],
        'avg_height': row['avg_height'],
        'dex_entry': row['dex_entry']
      }
    else:
      return f"Pokémon with name {name} not found."
  except Exception as e:
    return f"Error fetching Pokémon data: {e}"

@anvil.server.callable
def add_pokemon(region, id, name, category, type, avg_height, avg_weight, dex_entry):
  # Add a new Pokémon to the Pokedex Data Table
  app_tables.pokemon.add_row(
    region=region,
    id=id,
    name=name,
    category=category,
    type=type,
    avg_height=avg_height,
    avg_weight=avg_weight,
    dex_entry=dex_entry
  )
  return f"Successfully added Pokémon {name} to the Pokedex!"