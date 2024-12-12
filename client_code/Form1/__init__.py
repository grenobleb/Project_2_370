from ._anvil_designer import Form1Template
import anvil.server
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.populate_regions()

    def populate_regions(self):
        # Fetch regions from the server
        regions = anvil.server.call('get_regions')
        self.dropDownRegion.items = [(region, region) for region in regions]

    def dropDownRegion_change(self, **event_args):
        # Fetch Pokémon for the selected region
        selected_region = self.dropDownRegion.selected_value
        if selected_region:
            pokemon_list = anvil.server.call('get_pokemon_by_region', selected_region)
            self.dropDownPokemon.items = [(p['name'], p['id']) for p in pokemon_list]
            self.dropDownPokemon.enabled = True
        else:
            self.dropDownPokemon.items = []
            self.dropDownPokemon.enabled = False

    def dropDownPokemon_change(self, **event_args):
        # Fetch details for the selected Pokémon
        selected_pokemon_id = self.dropDownPokemon.selected_value
        if selected_pokemon_id:
            pokemon_details = anvil.server.call('get_pokemon_details', selected_pokemon_id)
            if pokemon_details:
                # Populate UI fields with Pokémon details
                self.Pkm.text = f"Name: {pokemon_details['name']}"
                self.PkmId.text = f"Id: {pokemon_details['id']}"
                self.PkmCategory.text = f"Category: {pokemon_details['category']}"
                self.PkmType.text = f"Type: {pokemon_details['type']}"
                self.PkmAvgWeight.text = f"Average Weight: {pokemon_details['avg_weight']} kg"
                self.PkmAvgHeightLabel.text = f"Average Height: {pokemon_details['avg_height']} m"
                self.PkmEntry.text = f"Dex Entry: {pokemon_details['dex_entry']}"