from booking import Booking

class BookingManager:
    def create_booking(self, user, room):
        room.book()
        return Booking(user, room)
