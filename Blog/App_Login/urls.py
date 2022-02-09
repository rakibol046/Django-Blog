from django.urls import path
from . import views
app_name = 'App_Login'
urlpatterns = [
   path('signup/', views.signup, name='signup'),
   path('login/', views.login_page, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('profile-update/', views.user_profile_update, name='profile_update'),
   path('add-profile-pic/', views.add_profile_pic, name='add_profile_pic'),
   path('update-profile-pic/', views.update_profile_pic, name='update_profile_pic'), 
   

]
