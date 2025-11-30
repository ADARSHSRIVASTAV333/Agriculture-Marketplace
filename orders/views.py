from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Order, OrderItem
from .forms import CheckoutForm
from products.models import Product
import uuid

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum([item.subtotal for item in cart_items])
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'orders/cart.html', context)

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if product.stock <= 0:
        messages.error(request, 'Product is out of stock.')
        return redirect('products:product_detail', pk=pk)
    
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            messages.error(request, 'Cannot add more than available stock.')
    else:
        messages.success(request, 'Added to cart!')
    
    return redirect('orders:cart')

@login_required
def update_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity <= 0:
            cart_item.delete()
            messages.success(request, 'Item removed from cart.')
        elif quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            messages.error(request, 'Quantity exceeds available stock.')
    
    return redirect('orders:cart')

@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('orders:cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    if not cart_items:
        messages.error(request, 'Your cart is empty.')
        return redirect('orders:cart')
    
    total = sum([item.subtotal for item in cart_items])
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = form.save(commit=False)
            order.user = request.user
            order.order_number = f"ORD{uuid.uuid4().hex[:10].upper()}"
            order.total_amount = total
            order.save()
            
            # Create order items and update stock
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
                
                # Update product stock
                product = cart_item.product
                product.stock -= cart_item.quantity
                product.save()
            
            # Clear cart
            cart_items.delete()
            
            messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
            return redirect('orders:order_detail', pk=order.pk)
    else:
        form = CheckoutForm(initial={
            'shipping_address': request.user.address,
            'shipping_phone': request.user.phone,
        })
    
    context = {
        'form': form,
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
