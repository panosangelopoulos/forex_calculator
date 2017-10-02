# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pair(models.Model):
    name = models.CharField(max_length=256)
    base_currency = models.CharField(max_length=256)
    second_currency = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=4, max_digits=6)

    def __str__(self):
        return self.name