from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

class PostsList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer