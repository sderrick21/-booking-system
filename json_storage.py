<<<<<<< HEAD
import json

class JsonStorage:
    @staticmethod
    def save(data):
        with open("data.json", "w") as file:
            json.dump(data, file)
=======
print("JSON STORAGE FILE LOADED")

import json

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
>>>>>>> 2591b35fe8fa49a6f973792dc5568ab88b27b350
