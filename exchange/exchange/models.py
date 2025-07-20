from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)
    kyc_passport = models.FileField(upload_to='kyc/', null=True, blank=True)
    kyc_status = models.CharField(max_length=20, choices=[('pending','На проверке'), ('approved','Одобрено'), ('rejected','Отклонено')], default='pending')
    referral_code = models.CharField(max_length=16, unique=True)
    invited_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    deals_count = models.PositiveIntegerField(default=0)
    is_blocked = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    balance_usdt = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    telegram_id = models.CharField(max_length=32, null=True, blank=True)

class FiatPayment(models.Model):
    name = models.CharField(max_length=30)  # Qiwi, ЮMoney, PayPal, etc.

class Offer(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    crypto_currency = models.CharField(max_length=10) # BTC, ETH, USDT
    fiat_currency = models.CharField(max_length=10) # RUB, USD, EUR, etc.
    payment_method = models.ForeignKey(FiatPayment, on_delete=models.CASCADE)
    min_amount = models.DecimalField(max_digits=12, decimal_places=2)
    max_amount = models.DecimalField(max_digits=12, decimal_places=2)
    rate = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Deal(models.Model):
    buyer = models.ForeignKey(UserProfile, related_name='buyer_deals', on_delete=models.CASCADE)
    seller = models.ForeignKey(UserProfile, related_name='seller_deals', on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=16, choices=[
        ('created','Создана'),('paid','Оплачена'),('released','Завершена'),('dispute','Спор'),('cancelled','Отменена')
    ])
    commission_rate = models.DecimalField(max_digits=4, decimal_places=2)
    commission_buyer = models.DecimalField(max_digits=12, decimal_places=2)
    commission_seller = models.DecimalField(max_digits=12, decimal_places=2)
    frozen = models.BooleanField(default=False)
    dispute_reason = models.TextField(blank=True)
    dispute_files = models.FileField(upload_to='disputes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class SupportTicket(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
