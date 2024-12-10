import anvil.server
from pymongo import MongoClient

# Connect to mongodb
MONGO_URI = "mongodb+srv://localhost:27017@cluster0.mongodb.net/Project2?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['Project2']  # Replace with your database name
pokedex = db['Pokedex']  # Replace with your collection name

@anvil.server.callable
def getPokemon(region):
  # Query the MongoDB collection
  document = pokedex.find_one({"Region": region})
  if document:
    return {
      "firstPokemon": document.get("firstPokemon"),
      "lastPokemon": document.get("lastPokemon")
    }
  else:
    return None  # Return None if no document matches