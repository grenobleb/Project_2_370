from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def dropDownRegion_change(self, **event_args):
    """Triggered when the region dropdown selection changes."""
    selected_region = self.dropDownRegion.selected_value
    if selected_region:
      # Call the server function to get Pokémon for the selected region
      pokemon_list = anvil.server.call('get_pokemon_by_region', selected_region)
      
      # Update the Pokémon dropdown
      self.dropDownPokemon.items = [(pokemon, pokemon) for pokemon in pokemon_list]
    else:
      # Clear the Pokémon dropdown if no region is selected
      self.dropDownPokemon.items = []
  
  def dropDownRegion_change(self, **event_args):
    """Triggered when the user selects and item from the dropdown menu."""
    region = self.dropDownRegion.selected_value  # Get selected region
    result = anvil.server.call('getPokemon', region)
      
    if result:
      self.firstPokemon.text = f"First Pokemon: {result['firstPokemon']}"
      self.lastPokemon.text = f"Last Pokemon: {result['lastPokemon']}"
    else:
      self.firstPokemon.text = "Region not found."
      self.lastPokemon.text  = "Region not found."
