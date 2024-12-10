from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from pymongo import MongoClient

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def dropDownRegion_change(self, **event_args):
    """Triggered when the region dropdown selection changes."""
    self.selectedRegion.text = self.dropDownRegion.selected_value
    testSelectedRegion = self.dropDownRegion.selected_value
    if testSelectedRegion:
      # Call the server function to get Pokémon for the selected region
      pokemon_list = anvil.server.call('get_pokemon_by_region', selected_region)
      
      # Update the Pokémon dropdown
      self.dropDownPokemon.items = [(pokemon, pokemon) for pokemon in pokemon_list]
    else:
      # Clear the Pokémon dropdown if no region is selected
      self.dropDownPokemon.items = []

  def dropDownPokemon_change(self, **event_args):
    self.Pkm.text = self.dropDownPokemon.text
    pokemonData = get_pokemon_data(self.Pkm.text)
    if pokemonData:
      # To access and display the ID:
      PkmId = pokemonData["id"]  # This is how you access the 'id' field in the dictionary
      # Assuming self.PkmId.text is an attribute in your UI element (e.g., a label in Tkinter or PyQt)
      self.PkmId.text = str(PkmId)  # Set the text to the Pokémon ID
    else:
      self.PkmId.text = "Pokémon not found"
    