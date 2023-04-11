from rest_framework import serializers
from . import models
#from tag.serializers import TagSerializer
#from categoria.serializers import CategoriaSerializer

class PostSerializer(serializers.ModelSerializer):
    
    #categoria = CategoriaSerializer()
    #tag = TagSerializer(read_only=True, many=True)
    
    class Meta:
        fields = ('id', 'title', 'content', 'author', 'abstract', 'cover_img','created_at', 'published_at', 'is_featured','slug' )
        model = models.Post