```python
Book.objects.filter(pk=1).delete()
# (1, {'bookshelf.Book': 1})

books = Book.objects.all()
print(books)

# <QuerySet []>
```
 