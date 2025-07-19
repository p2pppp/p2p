from django import forms
from .models import Currency

class ExchangeForm(forms.Form):
    amount = forms.FloatField(min_value=0.0001, label="Сумма обмена")
    from_currency = forms.ModelChoiceField(queryset=Currency.objects.all(), label="Отдаю")
    to_currency = forms.ModelChoiceField(queryset=Currency.objects.all(), label="Получаю")
