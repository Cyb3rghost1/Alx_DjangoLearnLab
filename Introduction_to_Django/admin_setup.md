# Django Admin Setup for Book Model

## Admin Configuration

The Book model has been registered with Django admin interface with the following customizations:

### BookAdmin Class Features:
- **list_display**: Shows title, author, and publication_year in the admin list view
- **list_filter**: Provides filtering options by author and publication_year
- **search_fields**: Enables searching by title and author

## Setup Steps:

1. **Register Model**: Book model registered in `bookshelf/admin.py`
2. **Create Superuser**: Run `python manage.py createsuperuser` to create admin account
3. **Access Admin**: Visit `http://127.0.0.1:8000/admin/` after running the server

## Admin Interface Features:
- View all books in a table format
- Filter books by author or publication year
- Search books by title or author name
- Add, edit, and delete book entries through the web interface