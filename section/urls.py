from django.urls import path, include
from rest_framework import routers

from . import views

class SectionView(routers.APIRootView):
    """
    API for Section Models
    """
    pass 
class SectionRouter(routers.DefaultRouter):
    APIRootView = SectionView

router = SectionRouter()

router.register(r'menu', views.MenuView, 'menu')
router.register(r'header', views.HeaderView, 'header')
router.register(r'footer', views.FooterView, 'footer')
router.register(r'media-gallery', views.MediaGalleryView, 'media-gallery')
router.register(r'slider', views.SliderView, 'slider')

urlpatterns = [
    path('', include(router.urls)),
]