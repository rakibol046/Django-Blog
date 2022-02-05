
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),   
]