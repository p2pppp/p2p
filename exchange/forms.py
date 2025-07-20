from django import forms
from .models import Currency

class ExchangeForm(forms.Form):
    amount = forms.FloatField(min_value=0.0001, label="Сумма обмена")
    from_currency = forms.ModelChoiceField(queryset=Currency.objects.all(), label="Отдаю")
    to_currency = forms.ModelChoiceField(queryset=Currency.objects.all(), label="Получаю")

    def clean(self):
        cleaned_data = super().clean()
        from_cur = cleaned_data.get('from_currency')
        to_cur = cleaned_data.get('to_currency')
        if from_cur == to_cur:
            raise forms.ValidationError("Валюты для обмена должны отличаться.")
        return cleaned_data
