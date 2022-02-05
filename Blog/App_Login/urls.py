from django.urls import path
from . import views
app_name = 'App_Login'
urlpatterns = [
   path('signup/', views.Signup, name='signup')
]
