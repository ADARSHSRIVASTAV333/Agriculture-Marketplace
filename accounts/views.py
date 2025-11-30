from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please login.')
            if user.role == 'seller':
                messages.info(request, 'Your seller account is pending admin approval.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.role == 'seller' and not user.is_approved:
                messages.error(request, 'Your seller account is pending approval.')
                return redirect('accounts:login')
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def dashboard(request):
    user = request.user
    context = {'user': user}
    
    if user.role == 'farmer':
        from orders.models import Order
        context['orders'] = Order.objects.filter(user=user)
        return render(request, 'accounts/farmer_dashboard.html', context)
    
    elif user.role == 'seller':
        from products.models import Product
        from orders.models import OrderItem
        context['products'] = Product.objects.filter(seller=user)
        context['orders'] = OrderItem.objects.filter(product__seller=user)
        return render(request, 'accounts/seller_dashboard.html', context)
    
    elif user.role == 'admin' or user.is_superuser:
        from products.models import Product
        from orders.models import Order
        context['total_users'] = User.objects.count()
        context['total_products'] = Product.objects.count()
        context['total_orders'] = Order.objects.count()
        context['pending_sellers'] = User.objects.filter(role='seller', is_approved=False)
        return render(request, 'accounts/admin_dashboard.html', context)
    
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form})
