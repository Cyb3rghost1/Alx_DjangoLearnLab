#!/usr/bin/env python
import os
import sys
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Introduction_to_Django.settings')
django.setup()

from accounts.models import CustomUser

# Test custom user creation
def test_custom_user():
    # Create a regular user
    user = CustomUser.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        date_of_birth=date(1990, 1, 1)
    )
    print(f"Created user: {user.username}")
    print(f"Date of birth: {user.date_of_birth}")
    print(f"Profile photo: {user.profile_photo}")
    
    # Create a superuser
    superuser = CustomUser.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123',
        date_of_birth=date(1985, 5, 15)
    )
    print(f"Created superuser: {superuser.username}")
    print(f"Is staff: {superuser.is_staff}")
    print(f"Is superuser: {superuser.is_superuser}")

if __name__ == '__main__':
    test_custom_user()