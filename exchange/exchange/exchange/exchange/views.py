from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ExchangeForm
from .models import Currency, Transaction
from django.contrib.auth.decorators import login_required
from .models import Offer

# Пример статических курсов (для MVP, позже интеграция с API)
RATES = {
    ('USDT', 'BTC'): 1/65000,
    ('BTC', 'USDT'): 65000,
    ('USDT', 'ETH'): 1/3500,
    ('ETH', 'USDT'): 3500,
    ('BTC', 'ETH'): 65000/3500,
    ('ETH', 'BTC'): 3500/65000,
}

COMMISSION = 0.005 # 0.5%

@login_required
def exchange(request):
    form = ExchangeForm(request.POST or None)
    result = None
    if request.method == 'POST' and form.is_valid():
        amount = form.cleaned_data['amount']
        from_cur = form.cleaned_data['from_currency'].code
        to_cur = form.cleaned_data['to_currency'].code
        rate = RATES.get((from_cur, to_cur), None)
        if rate:
            result_amount = amount * rate * (1 - COMMISSION)
            commission_amount = amount * rate * COMMISSION
            # Здесь интеграция с реальным API для отправки средств!
            txn = Transaction.objects.create(
                user=request.user,
                from_currency=form.cleaned_data['from_currency'],
                to_currency=form.cleaned_data['to_currency'],
                amount=amount,
                rate=rate,
                result_amount=result_amount,
                commission=commission_amount,
                status='pending'
            )
            result = {
                'result_amount': result_amount,
                'commission': commission_amount,
                'rate': rate
            }
    return render(request, 'exchange/exchange.html', {'form': form, 'result': result})
@login_required
def cabinet(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'exchange/cabinet.html', {'transactions': transactions})
def offers_list(request):
    # фильтры по валюте, сумме, платежке
    currency = request.GET.get('crypto')
    fiat = request.GET.get('fiat')
    payment = request.GET.get('payment')
    min_sum = request.GET.get('min')
    max_sum = request.GET.get('max')
    offers = Offer.objects.filter(is_active=True)
    if currency:
        offers = offers.filter(crypto_currency=currency)
    if fiat:
        offers = offers.filter(fiat_currency=fiat)
    if payment:
        offers = offers.filter(payment_method__name=payment)
    if min_sum:
        offers = offers.filter(min_amount__lte=min_sum)
    if max_sum:
        offers = offers.filter(max_amount__gte=max_sum)
    # ...
    return render(request, 'exchange/offers_list.html', {'offers': offers})
