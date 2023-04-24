from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from . import models


class ProductCategorySerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True)

    class Meta:
        fields = ('id', 'url', 'name', 'children')
        model = models.ProductCategory


class ProductSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer()

    class Meta:
        fields = ('id', 'title', 'description', 'sku', 'iframe_soundcloud_large', 'iframe_soundcloud_small', 'price',
                  'image', 'file', 'created_at', 'last_update', 'url', 'category')
        model = models.Product
