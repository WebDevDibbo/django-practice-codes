from django.db import models


class BankStatus(models.Model):
    is_bankrupt = models.BooleanField(default =False)