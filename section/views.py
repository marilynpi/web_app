from rest_framework import generics, viewsets
from .models import Menu, Header, Footer, MediaGallery, Slider
from .serializers import MenuSerializer, HeaderSerializer, FooterSerializer, MediaGallerySerializer, SliderSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

""" class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 
 """
class HeaderView(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

""" class HeaderList(generics.ListAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
class HeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
 """
class FooterView(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

""" class FooterList(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class FooterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
 """
class MediaGalleryView(viewsets.ModelViewSet):
    queryset = MediaGallery.objects.all()
    serializer_class = MediaGallerySerializer

""" class MediaGalleryList(generics.ListAPIView):
    queryset = MediaGallery.objects.all()
    serializer_class = MediaGallerySerializer
class MediaGalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaGallery.objects.all()
    serializer_class = MediaGallerySerializer """
class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

""" class SliderList(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
class SliderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer """
