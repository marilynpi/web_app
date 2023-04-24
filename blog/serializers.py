from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from . import models


class CategorySerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True)

    class Meta:
        fields = ('id', 'url', 'name', 'parent',
                  'children')
        model = models.Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'url', 'name')
        model = models.Tag


class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        fields = ('id',  'url', 'title', 'content', 'author', 'abstract',
                  'cover_image', 'created_at', 'last_update', 'is_featured', 'category', 'tags')
        model = models.Post
