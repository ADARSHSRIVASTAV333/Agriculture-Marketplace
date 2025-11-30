# 🛠️ Useful Django Commands

Quick reference for common Django management commands.

## 🚀 Getting Started

### Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Run Development Server
```bash
python manage.py runserver
```

### Run on Different Port
```bash
python manage.py runserver 8080
```

### Run on All Interfaces
```bash
python manage.py runserver 0.0.0.0:8000
```

## 💾 Database Commands

### Make Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Show Migrations
```bash
python manage.py showmigrations
```

### SQL for Migration
```bash
python manage.py sqlmigrate app_name migration_number
```

### Reset Database (Delete and Recreate)
```bash
# Windows
del db.sqlite3
python manage.py migrate

# Linux/Mac
rm db.sqlite3
python manage.py migrate
```

## 🔍 Inspection Commands

### Django Shell
```bash
python manage.py shell
```

### Database Shell
```bash
python manage.py dbshell
```

### Check for Issues
```bash
python manage.py check
```

### Show URLs
```bash
python manage.py show_urls  # If django-extensions installed
```

## 📦 Static Files

### Collect Static Files
```bash
python manage.py collectstatic
```

### Collect Without Prompts
```bash
python manage.py collectstatic --noinput
```

### Clear Static Files
```bash
python manage.py collectstatic --clear
```

## 👥 User Management

### Create Superuser
```bash
python manage.py createsuperuser
```

### Change User Password
```bash
python manage.py changepassword username
```

## 🗄️ Data Management

### Dump Data (Backup)
```bash
# All data
python manage.py dumpdata > backup.json

# Specific app
python manage.py dumpdata products > products_backup.json

# Exclude certain apps
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > backup.json
```

### Load Data (Restore)
```bash
python manage.py loaddata backup.json
```

### Flush Database (Clear all data)
```bash
python manage.py flush
```

## 🧪 Testing Commands

### Run All Tests
```bash
python manage.py test
```

### Run Specific App Tests
```bash
python manage.py test accounts
```

### Run Specific Test
```bash
python manage.py test accounts.tests.TestUserModel
```

### Run with Coverage
```bash
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 🔧 Development Commands

### Create New App
```bash
python manage.py startapp app_name
```

### Create Custom Management Command
```bash
# Create directory structure
mkdir -p app_name/management/commands
touch app_name/management/__init__.py
touch app_name/management/commands/__init__.py
touch app_name/management/commands/command_name.py
```

## 📊 Admin Commands

### Clear Sessions
```bash
python manage.py clearsessions
```

### Clear Cache
```bash
python manage.py clear_cache  # If django-extensions installed
```

## 🐍 Python Shell Commands

### Open Django Shell
```bash
python manage.py shell
```

### Common Shell Operations
```python
# Import models
from accounts.models import User
from products.models import Product, Category

# Get all objects
users = User.objects.all()
products = Product.objects.all()

# Get specific object
user = User.objects.get(id=1)
product = Product.objects.get(id=1)

# Filter objects
farmers = User.objects.filter(role='farmer')
active_products = Product.objects.filter(is_active=True)

# Create object
category = Category.objects.create(
    name='New Category',
    description='Description here'
)

# Update object
product.price = 100
product.save()

# Delete object
product.delete()

# Count objects
user_count = User.objects.count()

# Order objects
products = Product.objects.order_by('-created_at')

# Get or create
category, created = Category.objects.get_or_create(
    name='Seeds',
    defaults={'description': 'Seed products'}
)

# Exit shell
exit()
```

## 🔐 Security Commands

### Check Security Issues
```bash
python manage.py check --deploy
```

### Generate Secret Key
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## 📝 Custom Commands for This Project

### Setup Initial Data
```bash
python setup_data.py
```

### Create Sample Data (if script exists)
```bash
python manage.py create_sample_data
```

## 🐛 Debugging Commands

### Run with Debug Toolbar
```bash
# Install django-debug-toolbar first
pip install django-debug-toolbar
# Add to INSTALLED_APPS and middleware
python manage.py runserver
```

### Show SQL Queries
```python
# In Django shell
from django.db import connection
from products.models import Product

products = Product.objects.all()
print(connection.queries)
```

### Check for Missing Migrations
```bash
python manage.py makemigrations --dry-run
```

## 📦 Package Management

### Install Requirements
```bash
pip install -r requirements.txt
```

### Update Requirements
```bash
pip freeze > requirements.txt
```

### Install Specific Package
```bash
pip install package_name
```

### Uninstall Package
```bash
pip uninstall package_name
```

## 🌐 Production Commands

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Run with Gunicorn
```bash
gunicorn agrimarket.wsgi:application --bind 0.0.0.0:8000
```

### Run with uWSGI
```bash
uwsgi --http :8000 --module agrimarket.wsgi
```

## 🔄 Migration Commands

### Create Empty Migration
```bash
python manage.py makemigrations --empty app_name
```

### Fake Migration
```bash
python manage.py migrate --fake app_name migration_name
```

### Reverse Migration
```bash
python manage.py migrate app_name previous_migration_name
```

### Show Migration SQL
```bash
python manage.py sqlmigrate app_name migration_number
```

## 📊 Useful Shell Scripts

### Quick Reset (Development Only)
```bash
# Windows
del db.sqlite3
python manage.py migrate
python setup_data.py
python manage.py createsuperuser

# Linux/Mac
rm db.sqlite3
python manage.py migrate
python setup_data.py
python manage.py createsuperuser
```

### Full Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python setup_data.py
python manage.py createsuperuser
python manage.py runserver
```

## 🎯 Project-Specific Commands

### Create Categories
```bash
python setup_data.py
```

### Create Test Users (in shell)
```python
from accounts.models import User

# Create farmer
farmer = User.objects.create_user(
    username='farmer1',
    email='farmer@test.com',
    password='testpass123',
    role='farmer'
)

# Create seller
seller = User.objects.create_user(
    username='seller1',
    email='seller@test.com',
    password='testpass123',
    role='seller',
    is_approved=True
)
```

### Create Test Products (in shell)
```python
from products.models import Product, Category
from accounts.models import User

seller = User.objects.get(username='seller1')
category = Category.objects.first()

product = Product.objects.create(
    seller=seller,
    category=category,
    name='Test Product',
    description='Test description',
    price=100,
    stock=50,
    image='path/to/image.jpg'
)
```

## 💡 Tips

### Run Multiple Commands
```bash
# Windows
python manage.py makemigrations & python manage.py migrate & python manage.py runserver

# Linux/Mac
python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

### Background Process
```bash
# Linux/Mac
nohup python manage.py runserver &

# Windows (use separate terminal)
start python manage.py runserver
```

### Check Django Version
```bash
python -m django --version
```

### Check Python Version
```bash
python --version
```

### List Installed Packages
```bash
pip list
```

### Show Package Info
```bash
pip show django
```

## 🆘 Troubleshooting Commands

### Clear Python Cache
```bash
# Windows
del /s /q __pycache__
del /s /q *.pyc

# Linux/Mac
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

### Reset Migrations (Careful!)
```bash
# Delete migration files (keep __init__.py)
# Then:
python manage.py makemigrations
python manage.py migrate
```

### Check for Errors
```bash
python manage.py check
python manage.py check --deploy
```

## 📚 Help Commands

### General Help
```bash
python manage.py help
```

### Command-Specific Help
```bash
python manage.py help migrate
python manage.py help runserver
```

### List All Commands
```bash
python manage.py help
```

## 🎓 Learning Commands

### Interactive Shell with IPython
```bash
pip install ipython
python manage.py shell
```

### Django Extensions (Optional)
```bash
pip install django-extensions
# Add 'django_extensions' to INSTALLED_APPS
python manage.py shell_plus
python manage.py show_urls
python manage.py graph_models -a -o models.png
```

---

## 📝 Quick Reference Card

| Task | Command |
|------|---------|
| Run server | `python manage.py runserver` |
| Create admin | `python manage.py createsuperuser` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Open shell | `python manage.py shell` |
| Collect static | `python manage.py collectstatic` |
| Run tests | `python manage.py test` |
| Check issues | `python manage.py check` |
| Backup data | `python manage.py dumpdata > backup.json` |
| Restore data | `python manage.py loaddata backup.json` |

---

**Keep this file handy for quick reference!** 🚀
