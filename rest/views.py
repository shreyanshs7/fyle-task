# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import BankDetail
# Create your views here.

def index(request):
    return render(request,'index.html')

def getBranchDetails(request):
    if request.method == "POST":
        ifsc = request.POST.get('ifsc')
        if ifsc == "":
            return HttpResponse("Enter ifsc code !")

        try:
            allDetail = BankDetail.objects.get(ifsc__iexact=ifsc)
        except Exception as e:
            print(str(e))
            return HttpResponse("IFSC code not valid")    

        return render(request,'branchDetail.html',{"allDetail":allDetail})
    else:
        return HttpResponse("Method not valid")

def getAllBranch(request):
    if request.method == "POST":
        city = request.POST.get('city')
        bank = request.POST.get('bank')

        if city == "" and bank == "":
            return HttpResponse("Enter details !")

        elif city == "":
            return HttpResponse("Enter city !")
        elif bank == "":
            return HttpResponse("Enter bank !")


        try:
            allBranch = BankDetail.objects.filter(city__iexact=city,bank_name__iexact=bank)
        except Exception as e:
            print(str(e))

            return HttpResponse("No details")
        return render(request,'allBranch.html',{'allBranch':allBranch ,'city':city ,'bank':bank})    