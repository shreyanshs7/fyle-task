# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BankDetail(models.Model):
    ifsc = models.CharField(max_length=500)
    bank_id = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    bank_name = models.CharField(max_length=500)
