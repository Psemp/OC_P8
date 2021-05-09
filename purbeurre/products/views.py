from django.shortcuts import render, get_object_or_404
from research.models import Product

# Create your views here.


def detail(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    nutricon = f"https://static.openfoodfacts.org/images/attributes/nutriscore-{p.nutriscore}.svg"
    context = {"product": p, "nutricon": nutricon}
    return render(request, 'products/detail.html', context)
