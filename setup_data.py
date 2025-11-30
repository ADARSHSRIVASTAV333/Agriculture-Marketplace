"""
Script to create initial categories and sample data
Run this after migrations: python manage.py shell < setup_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrimarket.settings')
django.setup()

from products.models import Category

# Create categories
categories = [
    {'name': 'Seeds', 'description': 'High-quality seeds for various crops including wheat, rice, vegetables, and more'},
    {'name': 'Fertilizers', 'description': 'Organic and chemical fertilizers to boost crop growth and yield'},
    {'name': 'Pesticides', 'description': 'Effective pest control solutions for protecting your crops'},
    {'name': 'Tools', 'description': 'Agricultural tools and equipment for farming operations'},
    {'name': 'Irrigation', 'description': 'Irrigation systems and equipment for efficient water management'},
    {'name': 'Machinery', 'description': 'Agricultural machinery and equipment for modern farming'},
]

print("Creating categories...")
for cat_data in categories:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    if created:
        print(f"✓ Created category: {category.name}")
    else:
        print(f"- Category already exists: {category.name}")

print("\nSetup complete!")
print("\nNext steps:")
print("1. Create a superuser: python manage.py createsuperuser")
print("2. Run the server: python manage.py runserver")
print("3. Access the site at: http://127.0.0.1:8000/")
print("4. Access admin panel at: http://127.0.0.1:8000/admin/")
