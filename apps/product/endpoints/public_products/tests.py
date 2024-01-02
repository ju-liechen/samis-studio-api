from django.urls import reverse
from faker import Faker
from mixer.backend.django import mixer
from rest_framework.test import APITestCase

from apps.product.models import Product


class AdminRecordsTests(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.url = reverse('public-products')
        self.product_1 = mixer.blend(
            'product.Product',
        )
        self.product_2 = mixer.blend(
            'product.Product',
        )

    def test_public_products_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], Product.objects.count())
        self.assertEqual(response.data['results'][0]['id'],
                         self.product_1.id)
        self.assertEqual(response.data['results'][1]['id'],
                         self.product_2.id)
