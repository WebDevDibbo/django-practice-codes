
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addMusician, name ='add_musician'),
    path('edit/<int:id>', views.editMusician, name ='edit_musician'),
]
