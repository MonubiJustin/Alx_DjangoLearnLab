```python
from bookshelf.models import Book

# Retrieve the book
bk = Book.objects.get(title="1984")

# Update the title
bk.title = "Nineteen Eighty-Four"
bk.save() # save changes

print(bk)

# Expected Output:
# Nineteen Eighty-Four
```