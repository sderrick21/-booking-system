class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.is_booked = False

    def book(self):
        self.is_booked = True
