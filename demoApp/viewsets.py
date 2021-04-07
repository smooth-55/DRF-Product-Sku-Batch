from rest_framework import viewsets
from . import serializers, models


class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class SkuViewset(viewsets.ModelViewSet):
    queryset = models.Sku.objects.all()
    serializer_class = serializers.SkuSerializer

class BatchViewset(viewsets.ModelViewSet):
    queryset = models.Batch.objects.all()
    serializer_class = serializers.BatchSerializer