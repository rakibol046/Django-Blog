from django.urls import path
from . import views
app_name = 'App_Blog'
urlpatterns = [
   path('', views.Blog_List, name='blog_list')
]
