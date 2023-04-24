from django.urls import path, include
from rest_framework import routers

from . import views

class ShopView(routers.APIRootView):
    """
    API for Shop Models
    """
    pass 
class ShopRouter(routers.DefaultRouter):
    APIRootView = ShopView

router = ShopRouter()

router.register(r'product', views.ProductView, 'product')
router.register(r'product-category', views.ProductCategoryView, 'product-category')

urlpatterns = [
    path('', include(router.urls)),
]