from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('change_pass/', views.changePass, name='change_pass'),
    path('set_pass/', views.setPass, name='set_pass'),
]