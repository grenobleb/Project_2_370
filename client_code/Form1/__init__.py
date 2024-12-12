from ._anvil_designer import Form1Template
import anvil.server
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
      print(anvil.server.call('check_table_exists'))
