from django.shortcuts import get_object_or_404
from research.models import Product
from account.models import Profile
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


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
        product_id = kwargs['product_id']
        print(product_id)
        user_id = request.user.id
        user_profile = get_object_or_404(Profile, pk=user_id)
        user_profile.favorite.add(product_id)
        user_profile.save()
        return self.get(request, *args, **kwargs)
