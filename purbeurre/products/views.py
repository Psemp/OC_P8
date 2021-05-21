from django.shortcuts import get_object_or_404
from research.models import Product
from django.views.generic.base import TemplateView


class ProductView(TemplateView):

    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        product_id = kwargs['product_id']
        p = get_object_or_404(Product, pk=product_id)
        nutricon = f"https://static.openfoodfacts.org/images/attributes/nutriscore-{p.nutriscore}.svg"
        context = super().get_context_data(**kwargs)
        context = {"product": p, "nutricon": nutricon}
        return context

    def post(self, request, *args, **kwargs):
        print('post request')

        return self.get(request, *args, **kwargs)
