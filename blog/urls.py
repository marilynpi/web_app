from django.urls import path, include
from rest_framework import routers

from . import views

class BlogView(routers.APIRootView):
    """
    API for Blog Models
    """
    pass 
class BlogRouter(routers.DefaultRouter):
    APIRootView = BlogView

router = BlogRouter()

router.register(r'post', views.PostView, 'post')
router.register(r'category', views.CategoryView, 'category')
router.register(r'tag', views.TagView, 'tag')

urlpatterns = [
    path('', include(router.urls)),
]