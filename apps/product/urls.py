from django.urls import path

from .endpoints.public_products import views as public_products_views


urlpatterns = [
    path('public/product/products',
         public_products_views.PublicProductsListView.as_view(),
         name='public-products'),
]
