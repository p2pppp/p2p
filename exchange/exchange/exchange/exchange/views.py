from django.shortcuts import render, redirect
from .forms import ExchangeForm
from .models import Currency, Transaction
from django.contrib.auth.decorators import login_required

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
