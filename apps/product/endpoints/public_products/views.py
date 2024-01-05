from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.product.models import Product
from .serializers import PublicProductSerializer


class PublicProductsListView(generics.ListAPIView):
    serializer_class = PublicProductSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    ordering_fields = ['title', 'price', 'created_at']


class PublicProductsDetailView(generics.RetrieveAPIView):
    serializer_class = PublicProductSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
