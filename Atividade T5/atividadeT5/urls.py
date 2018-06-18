from django.contrib import admin
from django.urls import path
from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
] + core_urls
