class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
print(f"Book 1 Title: {book1.title}, Author: {book1.author}")
del book1.author

book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(f"Book 2 Title: {book2.title}, Author: {book2.author}")
