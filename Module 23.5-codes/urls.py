from django.urls import path
from . import views

urlpatterns = [
path('password_change/', views.UserPasswordChangeView.as_view(), name = 'change_pass'),
path('transfer/', views.TransferMoneyView.as_view(), name = 'transfer_money'),
]