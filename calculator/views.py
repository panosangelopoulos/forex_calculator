# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Pair

from forms import CalculateForm

import redis
# from datetime import datetime

from currencies import usd

# Create your views here.
pool = redis.ConnectionPool(host='calculateforex.redis.cache.windows.net', port=6379, db=0, password='loZUTa1RwhlKpoilC3DLqJa030xnkdFV+QhLGl3lot0=')
r = redis.Redis(connection_pool=pool)
usd_value = r.set('usd_val', usd, ex=30)


def index(request):
	profit = 0
	loss = 0
	currency = '$'
	if request.method == 'POST':
		form = CalculateForm(request.POST)
		if form.is_valid():
			target = form.cleaned_data['Target']
			entry = form.cleaned_data['Entry']
			stop = form.cleaned_data['Stop']
			lot = form.cleaned_data['Lot']
			account = form.cleaned_data['Account']
			position = form.cleaned_data['Position']

			# Calculations of Profit and Loss
			profit = calculate_profit_loss(entry, target, stop, lot, position)[0]
			loss = calculate_profit_loss(entry, target, stop, lot, position)[1]

			# Change value to Euro
			if account == 'EURO':
				profit = round(profit/usd, 2)
				loss = round(loss/usd, 2)
				currency = '€'
			form = CalculateForm()
	else :
		form = CalculateForm()
	return render(request, 'index.html', {'form' : form, 'profit': profit, 'currency' : currency, 'loss': loss})


def calculate_profit_loss(entry, target, stop, lot, position):
	if position == 'Sell':
		profit = float(lot) * 100000 *(float(entry) - float(target))
		loss = float(lot) * 100000 *(float(entry) - float(stop))
	else :
		profit = float(lot) * 100000 *(float(target) - float(entry))
		loss = float(lot) * 100000 *(float(stop) - float(entry))
	return profit , loss