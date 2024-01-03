import requests
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from faker import Faker
from apps.product.models import Product


def populate():
    fake = Faker()
    User = get_user_model()
    user = User.objects.create(
        email='hello@inputlogic.ca',
        is_staff=True,
        is_superuser=True,
    )
    user.set_password('superduper')
    user.save()

    products = []
    for _ in range(10):
        image_url = fake.image_url()

        response = requests.get(image_url)
        if response.status_code == 200:
            image = ContentFile(response.content, name=fake.file_name())

            product = Product(
                title=fake.job(),
                description=fake.sentence(),
                price=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                width=fake.pydecimal(left_digits=2, right_digits=1, positive=True),
                length=fake.pydecimal(left_digits=2, right_digits=1, positive=True),
                image=image
            )
            products.append(product)

    Product.objects.bulk_create(products)
