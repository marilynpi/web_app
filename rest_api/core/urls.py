"""
URL configuration for rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_volt.urls')),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/section/', include('section.urls')),
    path('api/v1/emails/', include('emails.urls')),
    path('api/v1/shop/', include('shop.urls')),
    path('api/v1/docs', include_docs_urls(title='REST API Documentation')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
