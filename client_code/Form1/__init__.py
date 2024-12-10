from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def dropDownRegion_change(self, **event_args):
    """This method is called when an item is selected"""
    #alert('You selected ' + self.dropDOwnRegion.selected_value)
    self.selectedRegion.text = self.dropDownRegion.selected_value
    tempFirstPokemon = app_tables.pokedex.get(region=self.dropDownRegion.selected_value)
    if tempFirstPokemon:
        self.firstPokemon.text = tempFirstPokemon['firstPokemon']
    else:
        self.firstPokemon.text = 'No data found'
    tempLastPokemon = app_tables.pokedex.get(region=self.dropDownRegion.selected_value)
    if tempLastPokemon:
        self.lastPokemon.text = tempLastPokemon['lastPokemon']
    else:
        self.lastPokemon.text = 'No data found'
