# Django Model Relationships

This app demonstrates three types of relationships between Django models:

## 1. ForeignKey (One-to-Many) Relationship

The `Book` model has a ForeignKey to the `Author` model:

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
```

This creates a one-to-many relationship where:
- One author can have many books
- Each book belongs to exactly one author

### Query Example:
```python
# Get all books by a specific author
author = Author.objects.get(name="George Orwell")
books = author.books.all()
```

## 2. ManyToMany Relationship

The `Library` model has a ManyToManyField to the `Book` model:

```python
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
```

This creates a many-to-many relationship where:
- One library can have many books
- One book can be in many libraries

### Query Example:
```python
# Get all books in a library
library = Library.objects.get(name="Central Library")
books = library.books.all()
```

## 3. OneToOne Relationship

The `Librarian` model has a OneToOneField to the `Library` model:

```python
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
```

This creates a one-to-one relationship where:
- Each library has exactly one librarian
- Each librarian manages exactly one library

### Query Example:
```python
# Get the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
```

## Admin Interface

The admin interface has been customized for each model:
- List displays show relevant fields
- Search fields enable quick lookups
- Filter options for related models
- Horizontal filter for many-to-many relationships