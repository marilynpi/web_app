from django.urls import path

from . import views

urlpatterns = [
    path('contact-form', views.ContactFormList.as_view()),
    path('contact-form/post', views.ContactFormPost.as_view()),
    path('contact-form/int:pk>', views.ContactFormDetail.as_view())
]