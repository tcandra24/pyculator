from models.config import Config
import json

FILE = 'config/config.json'

def load_config():
  with open(FILE, 'r') as file:
    data = json.load(file)
    return Config(**data)