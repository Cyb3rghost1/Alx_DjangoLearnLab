# Library Management System

This is my first Django project - a Library Management System built with Django.

## Project Setup

1. Navigate to the project directory:
   ```
   cd Introduction_to_Django
   ```

2. Start the development server:
   ```
   python manage.py runserver
   ```

3. Access the application at: http://127.0.0.1:8000/

## Project Structure

- **settings.py**: Configuration settings for the Django project
- **urls.py**: URL declarations for the project (the "table of contents")
- **manage.py**: Command-line utility for interacting with the project
- **db.sqlite3**: SQLite database file
- **wsgi.py**: WSGI application entry point for web servers
- **asgi.py**: ASGI application entry point for asynchronous web servers
- **__init__.py**: Makes this directory a Python package

## Development Notes

- Built with Django web framework
- Uses SQLite as the default database
- This directory contains the core configuration files for the Django project
- All Django apps should be created in this directory or as subdirectories