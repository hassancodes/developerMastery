class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):  # For print()
        return f"'{self.title}' by {self.author}"

    def __repr__(self): # For representation in lists, etc.
        return f"Book(title='{self.title}', author='{self.author}')"

    def __eq__(self, other):  # Equality check
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

# Usage
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Animal Farm", "George Orwell")

print(book1)        # Output: '1984' by George Orwell
print(repr(book1))  # Output: Book(title='1984', author='George Orwell')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False
