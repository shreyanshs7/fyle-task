# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import BankDetail
# Register your models here.
@admin.register(BankDetail)
class BankDetailAdmin(ImportExportModelAdmin):
    list_display = ['ifsc','branch','city','state']