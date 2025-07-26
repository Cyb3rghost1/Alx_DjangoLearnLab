# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")
print(f"Total books remaining: {Book.objects.count()}")
```

## Expected Output
```
Book deleted successfully
Total books remaining: 0
```