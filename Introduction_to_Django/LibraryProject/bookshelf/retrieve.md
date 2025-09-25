```python
book = Book.objects.get(pk=1)
```
```python
print(book.title)
# 1984
```

```python
print(book.author)
# George Orwell
```

```python
print(book.publication_year)
# 1949
```