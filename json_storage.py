import json

class JsonStorage:
    @staticmethod
    def save(data):
        with open("data.json", "w") as file:
            json.dump(data, file)
