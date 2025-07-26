"""
Script to create sample data for relationship_app models.
"""
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Introduction_to_Django.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # Create authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")
    author3 = Author.objects.create(name="Chinua Achebe")
    
    print(f"Created authors: {author1.name}, {author2.name}, {author3.name}")
    
    # Create books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author2)
    book4 = Book.objects.create(title="Things Fall Apart", author=author3)
    
    print(f"Created books: {book1.title}, {book2.title}, {book3.title}, {book4.title}")
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4)
    
    print(f"Created libraries: {library1.name}, {library2.name}")
    print(f"{library1.name} has {library1.books.count()} books")
    print(f"{library2.name} has {library2.books.count()} books")
    
    # Create librarians (OneToOne relationship)
    librarian1 = Librarian.objects.create(name="John Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Jane Doe", library=library2)
    
    print(f"Created librarians: {librarian1.name} for {librarian1.library.name}, {librarian2.name} for {librarian2.library.name}")
    
    # Demonstrate queries from query_samples.py
    from relationship_app.query_samples import get_books_by_author, get_books_in_library, get_librarian_for_library
    
    print("\nDemonstrating queries:")
    print(f"Books by {author1.name}: {', '.join([book.title for book in get_books_by_author(author1.name)])}")
    print(f"Books in {library1.name}: {', '.join([book.title for book in get_books_in_library(library1.name)])}")
    print(f"Librarian for {library1.name}: {get_librarian_for_library(library1.name).name}")

if __name__ == "__main__":
    # Clear existing data
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    
    # Create new sample data
    create_sample_data()