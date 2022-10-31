from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog', include('blog.urls')),
    path('brand', include('brand.urls')),
    path('mobil', include('mobil.urls')),
]
