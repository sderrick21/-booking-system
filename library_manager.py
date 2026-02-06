from book import Book

class LibraryManager:
    def __init__(self):
        self.books = []

    def load_books(self, data):
        self.books = []
        for item in data:
            self.books.append(Book(item["id"], item["title"]))

    def view_books(self):
        for book in self.books:
            print(book)
