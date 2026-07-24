from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):

    query = request.GET.get('q')
    category = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    return render(request, 'store/home.html', {
        'products': products,
        'query': query,
        'category': category
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'store/product_detail.html', {
        'product': product
    })

def contact(request):
    return render(request, 'store/contact.html')