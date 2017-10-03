from django import forms
from django.forms import ModelForm

CURRENCIES_CHOICES = (
    ('USD', 'usd'),
    ('EURO', 'euro'),
)

CURRENCIES_PAIRS = (
	('EURUSD', 'EURUSD'),
	('GBPUSD', 'GBPUSD'),
	('USDCAD', 'USDCAD'),
	('USDCHF', 'USDCHF'),
	('NZDUSD', 'NZDUSD'),
	('AUDUSD', 'AUDUSD'),
	('GBPJPY', 'GBPJPY'),
	('GBPCHF', 'GBPCHF'),
	('USDJPY', 'USDJPY'),
	)

POSITIONS = (
	('Buy', 'Buy/Long'),
	('Sell', 'Sell/Short')
	)


class CalculateForm(forms.Form):
	Position = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control col-lg-10'}), label='Position', choices=POSITIONS)
	Lot = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10', 'value' : 1}), label='Lot Size')
	Entry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10', 'value' : 1.2000}), label='Entry Price')
	Pair = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control col-lg-10'}), choices=CURRENCIES_PAIRS)
	Target = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10', 'value' : 1.2020}), label='Target Price')
	Stop = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-lg-10', 'value' : 1.1980}), label='Stop Loss')
	Account = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control col-lg-10'}), label='Account Currency', choices=CURRENCIES_CHOICES)




