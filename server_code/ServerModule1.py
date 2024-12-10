import anvil.server
from pymongo import MongoClient

# Connect to mongodb
MONGO_URI = "mongodb+srv://localhost:27017@cluster0.mongodb.net/Project2?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['Project2']  # Replace with your database name
pokedex = db['kanto_pokemon']  # Replace with your collection name

@anvil.server.callable
def get_pokemon_by_region(region):
    """Retrieve all Pokémon for a given region."""
    document = pokedex.find_one({"Region": region})
    if document:
        return document.get("Pokemon", [])  # Return the list of Pokémon or an empty list
    return []  # Return an empty list if no document matches

def get_pokemon_data(selected_name):
    # Query for the Pokémon by name
    query = {"name": selected_name}
    result = pokedex.find_one(query)  # Get the first matching document
    
    # Handle case if no result is found
    if result:
        return {
            "id": result.get("id"),
            "name": result.get("name"),
            "category": result.get("category"),
            "typing": result.get("typing"),
        }
    else:
        return f"Pokémon '{selected_name}' not found in the database."