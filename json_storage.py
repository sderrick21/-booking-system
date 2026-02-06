import json

class JsonStorage:
    @staticmethod
    def save(data):
        with open("data.json", "w") as file:
            json.dump(data, file)
    
    @staticmethod
    def load():
        try:
            with open("data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
