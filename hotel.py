from room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, number, price):
        self.rooms.append(Room(number, price))

    def available_rooms(self):
        return [room for room in self.rooms if not room.is_booked]
