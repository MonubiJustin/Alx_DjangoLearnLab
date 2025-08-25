```python
from bookshelf.models import Book

# Create a Book instance
bk = Book(title="1984", author="George Orwell", publication_year=1949) 
bk.save() # save to databse

print(bk)

# Expected Output:
# 1984
```