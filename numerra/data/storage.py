import json

FILE = 'numerra/data/histories.json'

def push_data(data):
  with open(FILE, 'w') as file:
    json.dump(data, file, indent=2)

def show_data():
  with open(FILE, 'r') as file:
    return json.load(file)