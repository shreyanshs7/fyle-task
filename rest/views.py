# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import BankDetail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def getBranchDetails(request):
    data = {}
    if request.method == "POST":
        ifsc = request.POST.get('ifsc')
        if "ifsc" not in request.POST:
            data['success'] = False
            data['message'] = "Enter ifsc code"

            return JsonResponse(data,safe=False)

        try:
            allDetail = BankDetail.objects.get(ifsc__iexact=ifsc)
        except Exception as e:
            print(str(e))
            data['success'] = False
            data['message'] = "No details found" 

            return JsonResponse(data,safe=False)   

        detailsList = []

        tempData = {
                'ifsc': allDetail.ifsc,
                'bank_id' : allDetail.bank_id,
                'branch' : allDetail.branch,
                'address' : allDetail.address,
                'city' : allDetail.city,
                'district' : allDetail.district,
                'state' : allDetail.state,
                'bank_name': allDetail.bank_name
            }

        detailsList.append(tempData)   

        data['success'] = True
        data['details'] = detailsList

        return JsonResponse(data,safe=False)       
        
    else:
        data['success'] = False
        data['message'] = "Method not valid"

        return JsonResponse(data,safe=False)

@csrf_exempt
def getAllBranch(request):
    data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        bank = request.POST.get('bank')

        if "city" not in request.POST and "bank" not in request.POST:
            data['success'] = False
            data['message'] = "Enter city and bank"

            return JsonResponse(data,safe=False)

        if "city" not in request.POST:
            data['success'] = False
            data['message'] = "Enter city"

            return JsonResponse(data,safe=False)

        if "bank" not in request.POST:
            data['success'] = False
            data['message'] = "Enter Bank"

            return JsonResponse(data,safe=False)


        
        allBranch = BankDetail.objects.filter(city__iexact=city,bank_name__iexact=bank)

        if allBranch.count() == 0:
            data['success'] = False
            data['message'] = "No details found for given city and bank"

            return JsonResponse(data,safe=False)
        
        
        branchList = []

        for obj in allBranch:
            tempData = {
                'ifsc' : obj.ifsc,
                'bank_id': obj.bank_id,
                'branch' : obj.branch,
                'address' : obj.address,
                'district' : obj.district,
                'state' : obj.state,

            }
            branchList.append(tempData)
            tempData = {}

        data['success'] = True
        data['details'] = branchList

        return JsonResponse(data,safe=False)     

    else:
        data['success'] = False
        data['message'] = "Method not allowed"    

        return JsonResponse(data,safe=False)