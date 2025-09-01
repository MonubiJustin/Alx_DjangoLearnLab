from .models import Author, Book, Library, Librarian

def run_queries():
    #1. Query all books by a specific author
    author_name = input("Enter author name: ").strip()
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")
        
    #2. List all books in a library
    try:
        library_name = input("Enter library Name: ").strip()
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print("-", book.title)
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
        
    #3. Retrieve a librarian for a library
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")
    except NameError:
        # In case 'library' wasn't found above
        print("Library not found, so librarian lookup skipped")