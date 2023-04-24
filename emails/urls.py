from django.urls import path

from . import views

urlpatterns = [
    path('contact-form/post', views.ContactFormPost.as_view()),
    path('billing/post', views.BillingPost.as_view()),
]