from ._anvil_designer import Form1Template
import anvil.server
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Initialize dropdowns
    self.load_regions()

  def load_regions(self):
    try:
      # Call the server to get the regions
      regions = anvil.server.call('get_regions')
      
      if regions:
        self.dropDownRegion.items = [(region, region) for region in regions]
      else:
        print("No regions found in the database.")
    except Exception as e:
      print(f"Error loading regions: {e}")

  def dropDownRegion_change(self, **event_args):
    # clear outputs
    self.selectedRegion.text = ""
    self.PkmId.text = ""
    self.Pkm.text = ""
    self.PkmCategory.text = ""
    self.PkmType.text = ""
    self.PkmAvgHeight.text = ""
    self.PkmAvgWeight.text = ""
    self.PkmEntry.text = ""
    
    # Get the selected region
    selected_region = self.dropDownRegion.selected_value
        
    if selected_region:
      self.selectedRegion.text = selected_region
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
      self.Pkm.text = selected_pokemon_name
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
        
        tempId = str(pokemon_data['id'])
        if (tempId is None or tempId == ""):
          self.PkmId.text = "No data currently available"
        else:
          self.PkmId.text = tempId
          
        tempCat = pokemon_data['category']
        if (tempCat is None or tempCat == ""): 
          self.PkmCategory.text = "No data currently available"
        else:
          self.PkmCategory.text = tempCat
          
        tempType = pokemon_data['type']
        if (tempType is None or tempType == ""):
          self.PkmType.text = "No data currently available"
        else:
          self.PkmType.text = tempType
        
        tempAvgH = f"{pokemon_data['avg_height']} m"
        if (tempAvgH is None or tempAvgH == " m" or tempAvgH == "None m"):
          self.PkmAvgHeight.text = "No data currently available"
        else:
          self.PkmAvgHeight.text = tempAvgH
        
        tempAvgW = f"{pokemon_data['avg_weight']} kg"
        if (tempAvgW is None or tempAvgW == " kg" or tempAvgH == "None kg"):
          self.PkmAvgWeight.text = "No data currently available"
        else:
          self.PkmAvgWeight.text = tempAvgW
        
        tempEntry = pokemon_data['dex_entry']
        if (tempEntry is None or tempEntry == ""):
          self.PkmEntry.text = "No data currently available"
        else:
          self.PkmEntry.text = tempEntry
        
      else:
        print(f"Error: {pokemon_data}")
    except Exception as e:
       print(f"Error displaying Pokémon data: {e}")

  def selectAddButton_click(self, **event_args):
    self.welcomeLabel.visible = False
    self.IntroLabel1.visible = False
    self.IntroLabel2.visible = False
    self.IntroLabel3.visible = False
    self.selectRegion.visible = False
    self.selectPokemon.visible = False
    self.selectAdd.visible = False
    self.addPokemon.visible = True
    pass

  def selectRemoveButton_click(self, **event_args):
    self.welcomeLabel.visible = False
    self.IntroLabel1.visible = False
    self.IntroLabel2.visible = False
    self.IntroLabel3.visible = False
    self.selectRegion.visible = False
    self.selectPokemon.visible = False
    self.selectAdd.visible = False
    self.removePokemon.visible = True
    pass

  def addPkm_click(self, **event_args):
    # Gather inputs
    tAddRegion = self.addRegion.text
    tAddId = self.addPkmId.text
    tAddName = self.addPkmName.text
    tAddCategory = self.addPkmCat.text
    tAddType = self.addPkmType.text
    tAddAvgHeight = self.addPkmAvgHeight.text
    tAddAvgWeight = self.addPkmAvgWeight.text
    tAddEntry = self.addPkmEntry.text

    # Validate inputs
    if (self.addPkmName.text is None):
      alert("Pokemon must be registered with a name")
      return

    # Call server to add Pokémon
    try:
      result = anvil.server.call(
        'add_pokemon',
        tAddRegion,
        tAddId,
        tAddName,
        tAddCategory,
        tAddType,
        tAddAvgHeight,
        tAddAvgWeight,
        tAddEntry
      )
      alert(result)

    except Exception as e:
      alert(f"Error adding Pokémon: {e}")

    self.addPkmDone.visible = True
    self.addPkmInfo2.visible = True
    self.addRegion.text = ""
    self.addPkmName.text = ""
    self.addPkmId.text = ""
    self.addPkmCat.text = ""
    self.addPkmType.text = ""
    self.addPkmAvgHeight.text = ""
    self.addPkmAvgWeight.text = ""
    self.addPkmEntry.tetx = ""

  def addPkmDone_click(self, **event_args):
    self.welcomeLabel.visible = True
    self.IntroLabel1.visible = True
    self.IntroLabel2.visible = True
    self.IntroLabel3.visible = True
    self.addPokemon.visible = False
    self.selectRegion.visible = True
    self.selectAdd.visible = True

  def removePkmButton_click(self, **event_args):
    pokemon_name = self.removePkm.text  # Get the name from the input box

    if pokemon_name:  # Ensure the name is not empty
        try:
            result = anvil.server.call('remove_pokemon_by_name', pokemon_name)
            alert(result)  # Display the result to the user
            self.removePkm.text = ""  # Clear the input box
        except Exception as e:
            alert(f"Error removing Pokémon: {e}")
    else:
        alert("Please enter a Pokémon name.")
    self.removePkmInfo3.visible = True
    self.removePkmInfo2.visible = True

  def removePkmDone_click(self, **event_args):
    self.welcomeLabel.visible = True
    self.IntroLabel1.visible = True
    self.IntroLabel2.visible = True
    self.IntroLabel3.visible = True
    self.removePokemon.visible = False
    self.selectRegion.visible = True
    self.selectAdd.visible = True
    
  