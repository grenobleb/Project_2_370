from ._anvil_designer import Form1Template
import anvil.server
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Initialize dropdowns
    self.load_regions()

  def load_regions(self):
    # Hardcode the regions or fetch them dynamically
    self.dropDownRegion.items = ['Kanto', 'Johto', 'Hoenn']  # You can dynamically fetch regions if needed

  def dropDownRegion_change(self, **event_args):
    # Get the selected region
    selected_region = self.dropDownRegion.selected_value
        
    if selected_region:
      self.selectAdd.visible = False
      self.selectPokemon.visible = True
      # Fetch Pokémon from the selected region
      self.populate_pokemon_dropdown(selected_region)

  def populate_pokemon_dropdown(self, region):
    try:
      # Call the server-side function to get Pokémon by region
      pokemon_data = anvil.server.call('get_pokemon_by_region', region)
            
      if pokemon_data:
        # Populate the Pokémon dropdown with names
        self.dropDownPkm.items = [pokemon[0] for pokemon in pokemon_data]  # Pokémon names are at index 0
        self.dropDownPkm.enabled = True  # Enable dropdown if data is available
      else:
        self.dropDownPkm.items = []
        self.dropDownPkm.enabled = False  # Disable if no Pokémon are found
    except Exception as e:
      print(f"Error populating Pokémon dropdown: {e}")

  def dropDownPkm_change(self, **event_args):
      
    # Get the selected Pokémon name
    selected_pokemon_name = self.dropDownPkm.selected_value
        
    if selected_pokemon_name:
      # Fetch the Pokémon data by name (get the full details)
      self.display_pokemon_data(selected_pokemon_name)
    else:
      print("No Pokemon Selected")

  def display_pokemon_data(self, pokemon_name):
    try:
      # Fetch the Pokémon data from the server
      pokemon_data = anvil.server.call('get_pokemon_by_name', pokemon_name)
            
      if isinstance(pokemon_data, dict):  # Ensure we got a dictionary (not an error string)
        self.PokemonInfo.visible = True
        # Display Pokémon data in labels
        if 
        self.selectedRegion.text = self.dropDownRegion.selected_value
        self.Pkm.text = self.dropDownPkm.selected_value
        self.PkmId.text = str(pokemon_data['id'])
        self.PkmCategory.text = pokemon_data['category']
        self.PkmType.text = pokemon_data['type']
        self.PkmAvgWeight.text = f"{pokemon_data['avg_weight']} kg"
        self.PkmAvgHeight.text = f"{pokemon_data['avg_height']} m"
        self.PkmEntry.text = pokemon_data['dex_entry']
      else:
        print(f"Error: {pokemon_data}")
    except Exception as e:
       print(f"Error displaying Pokémon data: {e}")

  def selectAddButton_click(self, **event_args):
    self.selectRegion.visible = False
    self.addPokemon.visible = True
    pass
