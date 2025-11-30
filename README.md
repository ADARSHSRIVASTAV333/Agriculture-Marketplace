# Online Agriculture Marketplace for Seeds and Tools

A complete Django-based e-commerce platform for agricultural products including seeds, fertilizers, pesticides, and tools.

## Features

### User Roles
- **Farmer (Buyer)**: Browse products, add to cart, place orders, write reviews
- **Seller (Supplier)**: Manage products (CRUD operations), view orders
- **Admin**: Approve sellers, manage users, categories, products, and orders

### Core Functionality
1. **User Authentication**
   - Registration with role selection
   - Login/Logout
   - Role-based dashboards
   - Profile management

2. **Product Management**
   - Categories: Seeds, Fertilizers, Pesticides, Tools
   - Product CRUD operations for sellers
   - Search and filter functionality
   - Product ratings and reviews
   - Stock management

3. **Shopping Cart & Orders**
   - Add/Update/Remove cart items
   - Checkout process
   - Cash on Delivery (COD) payment
   - Order tracking (Pending → Packed → Shipped → Delivered)
   - Order history

4. **Reviews & Ratings**
   - Buyers can review purchased products
   - Star rating system (1-5 stars)
   - Average rating display

5. **Additional Features**
   - Wishlist functionality
   - Blog/Guide section for farmers
   - Responsive design with Bootstrap 5
   - Admin panel for management

## Technology Stack
- **Backend**: Django 5.2.5
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Icons**: Font Awesome 6
- **Image Handling**: Pillow

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 4: Create Sample Categories (Optional)
```bash
python manage.py shell
```
Then run:
```python
from products.models import Category

categories = [
    {'name': 'Seeds', 'description': 'High-quality seeds for various crops'},
    {'name': 'Fertilizers', 'description': 'Organic and chemical fertilizers'},
    {'name': 'Pesticides', 'description': 'Pest control solutions'},
    {'name': 'Tools', 'description': 'Agricultural tools and equipment'},
]

for cat in categories:
    Category.objects.get_or_create(name=cat['name'], defaults={'description': cat['description']})

exit()
```

### Step 5: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage Guide

### For Farmers (Buyers)
1. Register with role "Farmer"
2. Browse products by category or search
3. Add products to cart
4. Proceed to checkout and place order
5. Track order status in dashboard
6. Write reviews for delivered products

### For Sellers
1. Register with role "Seller"
2. Wait for admin approval
3. After approval, login and access seller dashboard
4. Add products with details (name, category, price, stock, image)
5. Manage existing products (edit/delete)
6. View orders received

### For Admin
1. Login with superuser credentials
2. Access admin dashboard
3. Approve pending sellers
4. Manage categories, products, and orders
5. View reports and statistics
6. Access Django admin panel at `/admin/`

## Project Structure
```
agrimarket/
├── accounts/          # User authentication and profiles
├── products/          # Product and category management
├── orders/            # Cart and order management
├── reviews/           # Product reviews and ratings
├── blog/              # Blog posts and guides
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── media/             # User uploaded files
└── agrimarket/        # Project settings
```

## Key URLs
- Home: `/`
- Products: `/products/`
- Cart: `/orders/cart/`
- Login: `/accounts/login/`
- Register: `/accounts/register/`
- Dashboard: `/accounts/dashboard/`
- Admin Panel: `/admin/`
- Blog: `/blog/`

## Admin Panel Features
- User management with seller approval
- Category management
- Product moderation
- Order management and status updates
- Review moderation
- Blog post management

## Responsive Design
The application is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile phones

## Security Features
- CSRF protection
- Password validation
- User authentication required for sensitive operations
- Role-based access control
- Seller approval system

## Future Enhancements (Optional)
- Razorpay payment integration
- Real-time chat/messaging system
- Weather widget API integration
- Multi-language support (English + Hindi)
- Crop recommendation system
- Email notifications
- SMS notifications
- Advanced analytics and reports

## Troubleshooting

### Images not displaying
Make sure you have created the `media` folder and configured `MEDIA_URL` and `MEDIA_ROOT` in settings.

### Static files not loading
Run: `python manage.py collectstatic`

### Database errors
Delete `db.sqlite3` and run migrations again:
```bash
python manage.py migrate
```

## Deployment

### Deploy to Render (Recommended - Free Tier)
1. Create a [Render](https://render.com) account
2. Connect your GitHub repository
3. Click "New +" → "Blueprint" and select this repository
4. Render will automatically use `render.yaml` to configure deployment
5. Set environment variables:
   - `SECRET_KEY`: A secure random string
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render domain

### Deploy to Heroku/Railway
1. Use the included `Procfile` for deployment
2. Set the following environment variables:
   - `SECRET_KEY`: A secure random string
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your app domain
3. Run `./build.sh` as the build command

### Manual Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Run build script
./build.sh

# Start with gunicorn
gunicorn agrimarket.wsgi:application
```

## Support
For issues or questions, please check the Django documentation at https://docs.djangoproject.com/

## License
This project is created for educational purposes.
