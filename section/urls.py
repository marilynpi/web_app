from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.MenuList.as_view()),
    path('menu/<int:pk>/', views.MenuDetail.as_view()),
    path('header/', views.HeaderList.as_view()),
    path('header/<int:pk>/', views.HeaderDetail.as_view()),
    path('footer/', views.FooterList.as_view()),
    path('footer/<int:pk>/', views.FooterDetail.as_view()),
    path('media-gallery/', views.MediaGalleryList.as_view()),
    path('media-gallery/<int:pk>/', views.MediaGalleryDetail.as_view()),
    path('slider/', views.SliderList.as_view()),
    path('slider/<int:pk>/', views.SliderList.as_view()),
]