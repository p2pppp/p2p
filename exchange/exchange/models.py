from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True) # 'USDT', 'BTC', 'ETH'
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.code

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.ForeignKey(Currency, related_name='from_currency', on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, related_name='to_currency', on_delete=models.CASCADE)
    amount = models.FloatField()
    rate = models.FloatField()
    result_amount = models.FloatField()
    commission = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('done', 'Done'), ('failed', 'Failed')], default='pending')
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=20, unique=True)
    invited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')
class Fee(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    percent = models.FloatField(default=0.5)
