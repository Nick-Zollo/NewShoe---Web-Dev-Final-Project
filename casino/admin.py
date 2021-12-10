from django.contrib import admin
from .models import Balance, AllDeposits, AllWithdraws

# Register your models here.
admin.site.register(Balance)
admin.site.register(AllDeposits)
admin.site.register(AllWithdraws)
