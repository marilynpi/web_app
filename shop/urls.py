from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductsList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product-category/', views.ProductCategoriesList.as_view()),
    path('product-category/<int:pk>/', views.ProductCategoryDetail.as_view()),
]