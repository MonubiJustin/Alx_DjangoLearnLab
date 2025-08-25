```python
from bookshelf.models import Book

bk = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
bk.delete()

books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>   # Empty QuerySet indicates no books in the DB
```