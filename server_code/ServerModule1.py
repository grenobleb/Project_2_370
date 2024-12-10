import anvil.server
from pymongo import MongoClient

# Connect to mongodb
MONGO_URI = "mongodb+srv://localhost:27017@cluster0.mongodb.net/Project2?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['Project2']  # Replace with your database name
pokedex = db['Pokedex']  # Replace with your collection name

@anvil.server.callable
def get_pokemon_by_region(region):
    """Retrieve all Pokémon for a given region."""
    document = pokedex.find_one({"Region": region})
    if document:
        return document.get("Pokemon", [])  # Return the list of Pokémon or an empty list
    return []  # Return an empty list if no document matches