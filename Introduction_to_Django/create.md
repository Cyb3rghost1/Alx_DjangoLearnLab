# Create Operation

## Command
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

## Expected Output
```
# The book instance is created and saved to the database successfully.
# No output is displayed, but the book object is now stored in the database.
```