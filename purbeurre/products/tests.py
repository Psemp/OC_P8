from django.test import TestCase
from django.urls import reverse
from research.models import Product
# Create your tests here.


class CompareTestCase(TestCase):
    def setUp(self):

        p1 = Product(barcode=1111111111111, name='p1', url='https://p1.org/',
                     brand='b1', picture_url='https://p1p.org/', nutriscore='e', stores='s1')
        p1.save()

        self.product = Product.objects.get(name='p1')

    def test_detail_page_200(self):
        barcode = self.product.barcode
        response = self.client.get(reverse('detail', args=(barcode,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_404(self):
        barcode = self.product.barcode + 1
        response = self.client.get(reverse('detail', args=(barcode + 1,)))
        self.assertEqual(response.status_code, 404)
