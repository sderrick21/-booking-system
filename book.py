class Book:
    def __init__(self, book_id, title):
        self.id = book_id
        self.title = title

    def __str__(self):
        return f"{self.id} - {self.title}"