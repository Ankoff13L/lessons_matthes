import json

filename = 'numbers_favorit.json'

with open(filename) as f:
    filename = json.load(f)
    print(f"I know your favorite number! This {filename}.")



