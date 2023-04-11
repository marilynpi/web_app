from rest_framework import serializers
from . import models

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = '__all__'

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Menu
        fields =  ('id', 'name', 'items')

class HeaderSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = models.Header
        fields = ('id', 'name', 'logo', 'small_logo', 'featured_image','featured_image_mobile', 'menu')

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slider
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    
    class Meta:
        model = models.Footer
        fields = ('id', 'name', 'logo', 'menu', 'bottom_text')

class MediaGallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = models.MediaGallery