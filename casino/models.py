from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    balance = models.PositiveIntegerField(default=0)


class AllDeposits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    depositAmount = models.PositiveIntegerField(default=0)
    depositedAt = models.DateTimeField(auto_now_add=True, blank=True)


class AllWithdraws(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    withdrawAmount = models.PositiveIntegerField(default=0)
    withdrewAt = models.DateTimeField(auto_now_add=True, blank=True)


