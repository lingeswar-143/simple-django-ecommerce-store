from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import CartItem
from store.models import Product


@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart')

    total = sum(item.total_price() for item in cart_items)

    if request.method == "POST":

        order = Order.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            city=request.POST['city'],
            pincode=request.POST['pincode'],
            total_price=total
        )

        for item in cart_items:

            # Create order item
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            # Get latest product from database
            product = Product.objects.get(id=item.product.id)

            print(f"Before: {product.name} - Stock: {product.stock}")

            if product.stock >= item.quantity:
                product.stock -= item.quantity
                product.save(update_fields=["stock"])

            product.refresh_from_db()

            print(f"After: {product.name} - Stock: {product.stock}")

        # Clear cart
        cart_items.delete()

        return redirect('orders')

    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total": total
    })


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/orders.html',
        {'orders': orders}
    )