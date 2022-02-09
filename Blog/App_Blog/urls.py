from django.urls import path
from . import views
app_name = 'App_Blog'
urlpatterns = [
   path('', views.BlogList.as_view(), name='blog_list'),
   path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
   path('blog-details/<slug>', views.blog_details, name='blog_details'),
   path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
   path('edit-blog/<pk>', views.EditBlog.as_view(), name='edit_blog'),
   path('delete-blog/<pk>', views.delete_blog, name='delete_blog'),
]
