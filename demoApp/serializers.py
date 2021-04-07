from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sku
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Batch
        fields = '__all__'