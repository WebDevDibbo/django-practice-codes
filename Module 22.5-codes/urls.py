from django.urls import path
from .views import SendMoneyView, WithdrawMoneyView, TransferMoneyView

# app_name = 'transactions'
urlpatterns = [
    path('withdraw/', WithdrawMoneyView.as_view(), name = 'withdraw_money'),
    path('transfer/', TransferMoneyView.as_view(), name = 'transfer_money'),
]