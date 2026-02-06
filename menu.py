<<<<<<< HEAD
from user import User
from hotel import Hotel
from booking_manager import BookingManager
from json_storage import JsonStorage

def start_menu():
    hotel = Hotel("Simple Hotel")
    hotel.add_room(101, 100)
    hotel.add_room(102, 120)

    name = input("Enter your name: ")
    user = User(name)

    rooms = hotel.available_rooms()

    if not rooms:
        print("No rooms available")
        return

    print("Available rooms:")
    for room in rooms:
        print(room.number, room.price)

    choice = int(input("Select room number: "))

    for room in rooms:
        if room.number == choice:
            manager = BookingManager()
            booking = manager.create_booking(user, room)
            JsonStorage.save({"user": user.get_name(), "room": room.number})
            print("Room booked successfully")
=======
from library_manager import LibraryManager
from json_storage import load_data

def start_menu():
    manager = LibraryManager()

    while True:
        print("1. View Books")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            data = load_data()
            manager.load_books(data)
            manager.view_books()

        elif choice == "2":
            print("Goodbye")
            break
>>>>>>> 2591b35fe8fa49a6f973792dc5568ab88b27b350
