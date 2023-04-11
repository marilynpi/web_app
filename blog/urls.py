from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.PostsList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('category/', views.CategoriesList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('tag/', views.TagsList.as_view()),
    path('tag/<int:pk>/', views.TagDetail.as_view()),
]