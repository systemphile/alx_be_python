# Script contains definitions of classes implementing Ineritance and composition

# define parent class 
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{__class__.__name__}: {self.title} by {self.author}"

# define child classes with and initialize unique attributes for each
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self): # define unofficial display of the instance
        return f"{__class__.__name__}: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"{__class__.__name__}: {self.title} by {self.author}, Page Count: {self.page_count}"

# define composite class that will manage objects of other classes
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
    def list_books(self):
        for book in self.books:
            if isinstance(book, (Book, EBook, PrintBook)):
                print(book)