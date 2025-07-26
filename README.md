# Django Models Relationships

This project demonstrates complex relationships between Django models using ForeignKey, ManyToMany, and OneToOne fields.

## Project Structure

- **relationship_app**: App demonstrating model relationships
  - **Author**: Model with books (one-to-many relationship)
  - **Book**: Model with author (ForeignKey) and libraries (ManyToMany)
  - **Library**: Model with books (ManyToMany) and librarian (OneToOne)
  - **Librarian**: Model with library (OneToOne)

## Setup Instructions

1. Navigate to the project directory:
   ```
   cd django-models
   ```

2. Apply migrations:
   ```
   python manage.py makemigrations relationship_app
   python manage.py migrate
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

## Sample Queries

The `query_samples.py` file contains examples of:
- Querying books by a specific author (ForeignKey relationship)
- Listing all books in a library (ManyToMany relationship)
- Retrieving the librarian for a library (OneToOne relationship)