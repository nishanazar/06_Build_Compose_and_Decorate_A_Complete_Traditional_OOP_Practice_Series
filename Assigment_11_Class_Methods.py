class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
        

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


book1 = Book("python")
book2= Book("python")
book3 = Book("python")
print(Book.total_books)
