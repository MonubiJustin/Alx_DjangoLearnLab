```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.get(title="1984")

for book in books:
    print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949
```