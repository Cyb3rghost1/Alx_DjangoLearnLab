# CRUD Operations for Book Model

This document contains all CRUD operations performed on the Book model in the Django shell.

## 1. CREATE Operation
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Book instance created and saved to database successfully
```

## 2. RETRIEVE Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
# Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
```

## 3. UPDATE Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")
# Output:
# Updated Title: Nineteen Eighty-Four
```

## 4. DELETE Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")
print(f"Total books remaining: {Book.objects.count()}")
# Output:
# Book deleted successfully
# Total books remaining: 0
```

## Summary
All CRUD operations have been successfully implemented and documented. The Book model supports:
- Creating new book instances
- Retrieving existing books by title
- Updating book attributes
- Deleting book instances from the database