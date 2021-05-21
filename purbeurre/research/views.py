from django.shortcuts import render, get_object_or_404
from .script.compare import get_product_categories, get_similar_prod
from .script.compare import compare_products
from .models import Product

# Create your views here.


def index(request):
    return render(request, 'research/index.html')


def compare(request, product_id):
    user_product = get_object_or_404(Product, pk=product_id)
    cat_set = get_product_categories(user_product)
    similar_products = get_similar_prod(cat_set)
    better_products = compare_products(user_product, similar_products)
    context = {"better_products": better_products}
    return render(request, 'research/compare.html', context)
