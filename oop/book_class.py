# Script contains a Book class implementing magic methods

class Book:
    # implementing constructor, destructor and magic methods
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print(f"Deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"{__class__.__name__}('{self.title}', '{self.author}', {self.year})"