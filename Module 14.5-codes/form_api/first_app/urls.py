from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='first_app_homepage'),
    path('django_form/', views.djangoForm, name='django_form'),
    path('model_form/', views.modelForm, name='model_form'),
]