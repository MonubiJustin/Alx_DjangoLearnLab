```bash
In [27]: from bookshelf.models import Book
    ...: 
    ...: # Retrieve all books
    ...: books = Book.objects.all()
    ...: 
    ...: for book in books:
    ...:     print(book.title, book.author, book.publication_year)
    ...: 

In [30]: from bookshelf.models import Book
    ...: 
    ...: # Create a Book instance
    ...: bk = Book(title="1984", author="George Orwell", publi 
    ...: cation_year=1949)
    ...: bk.save() # save to databse
    ...: 
    ...: print(bk)
1984

In [31]: from bookshelf.models import Book
    ...: 
    ...: # Retrieve all books
    ...: books = Book.objects.all()
    ...: 
    ...: for book in books:
    ...:     print(book.title, book.author, book.publication_y 
    ...: ear)
    ...: 
1984 George Orwell 1949

In [32]: from bookshelf.models import Book
    ...: 
    ...: # Retrieve the book
    ...: bk = Book.objects.get(title="1984")
    ...: 
    ...: # Update the title
    ...: bk.title = "Nineteen Eighty-Four"
    ...: bk.save() # save changes
    ...: 
    ...: print(bk)
    ...: 
Nineteen Eighty-Four

In [33]: from bookshelf.models import Book
    ...: 
    ...: bk = Book.objects.get(title="Nineteen Eighty-Four")   
    ...: 
    ...: # Delete the book
    ...: bk.delete()
    ...: 
    ...: books = Book.objects.all()
    ...: print(books)
<QuerySet []>

In [34]: 
```