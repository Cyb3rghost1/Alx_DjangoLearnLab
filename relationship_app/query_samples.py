"""
Sample queries for relationship_app models demonstrating different relationship types.
"""

# Query all books by a specific author
def get_books_by_author(author_name):
    from relationship_app.models import Author
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# List all books in a library
def get_books_in_library(library_name):
    from relationship_app.models import Library
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    from relationship_app.models import Library
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None
    except AttributeError:
        return None  # No librarian assigned