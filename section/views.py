from rest_framework import generics

from .models import Menu, Header, Footer, MediaGallery, Slider
from .serializers import MenuSerializer, HeaderSerializer, FooterSerializer, MediaGallerySerializer, SliderSerializer

class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class HeaderList(generics.ListAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class HeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class FooterList(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class FooterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class MediaGalleryList(generics.ListAPIView):
    queryset = MediaGallery.objects.all()
    serializer_class = MediaGallerySerializer

class MediaGalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaGallery.objects.all()
    serializer_class = MediaGallerySerializer

class SliderList(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class SliderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer