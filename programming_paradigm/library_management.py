class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self, title):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False
        
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only books can be added")
    def check_out_book(self, title):
        for book in self._books:
            if isinstance(book, Book) and book.title == title:
                book.check_out(title=title)
    def return_book(self, title):
        for book in self._books:
            if isinstance(book, Book) and book.title == title:
                book.return_book(title=title)
    def list_available_books(self):
        for book in self._books:
            if isinstance(book, Book):
                print(f"{book.title} by {book.author}")