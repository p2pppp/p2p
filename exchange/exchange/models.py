from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)
    kyc_passport = models.FileField(upload_to='kyc/')
    kyc_status = models.CharField(max_length=20, choices=[('pending','На проверке'), ('approved','Одобрено'), ('rejected','Отклонено')], default='pending')
    referral_code = models.CharField(max_length=16, unique=True)
    invited_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    deals_count = models.PositiveIntegerField(default=0)
    is_blocked = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    balance_usdt = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # ...другие поля, например, по фиату
