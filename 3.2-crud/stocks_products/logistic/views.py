import django_filters
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title','description']

class StockFilter(django_filters.FilterSet):
    products=django_filters.CharFilter(field_name='positions__product')

    class Meta:
        model = Stock
        fields = ['products']

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_class = StockFilter
    search_fields = ['positions__product__title','positions__product__description']
