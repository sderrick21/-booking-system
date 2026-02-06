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

    try:
        choice = int(input("Select room number: "))
    except ValueError:
        print("Invalid room number")
        return

    for room in rooms:
        if room.number == choice:
            manager = BookingManager()
            manager.create_booking(user, room)
            JsonStorage.save({"user": user.get_name(), "room": room.number})
            print("Room booked successfully")
            return

    print("Selected room not available")
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
