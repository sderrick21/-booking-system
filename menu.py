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