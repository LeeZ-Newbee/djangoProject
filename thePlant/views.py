from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from thePlant import models
import json
from django import forms


# Create your views here.
def index(request):
    orderList = models.Order.objects.filter(invoice=True)
    needInvoice = models.Order.objects.filter(invoice=False)
    return render(request, 'index.html', {'orderList': orderList, 'needInvoice': needInvoice})


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'


# def addOrder(request):
#     models.Order.objects.create(date='2021-10-10', income=100, customer='张三', invoice=True)
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/profit/')
#         else:
#             return HttpResponse('表单验证失败')
#     else:
#         return HttpResponse('请求方式错误')

def addOrder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            date = data['dealDate']
            orderMoney = data['amountGet']
            customer = data['customerName']
            invoice = data['invoiceStatus']
            models.Order.objects.create(date=date, income=orderMoney, customer=customer, invoice=invoice)
            return redirect('/profit/')
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': '请求方式错误'}, status=405)


def profit(request):
    if request.method == 'POST':
        selectYear = request.POST.get('year')
        profitList = models.Order.objects.filter(date__year=selectYear)
        totalIncome = sum(item.income for item in profitList)
        costsList = models.Profit.objects.filter(date__year=selectYear)
        totalCosts = sum(item.cost for item in costsList)
        yearProfit = totalIncome - totalCosts
        return render(request, 'profit.html', {'totalIncome': totalIncome, 'totalCosts': totalCosts, 'yearProfit': yearProfit})
    return render(request, 'profit.html')


def login(request):
    return render(request, 'login.html')


def invoiceChange(request):
    dataBaseId = request.GET.get('invoiceId')
    models.Order.objects.filter(id=dataBaseId).update(invoice=True)
    return redirect('/index/')


def costs(request):
    if request.method == 'POST':
        select = request.POST.get('costCategory')
        cost = request.POST.get('costs')
        date = request.POST.get('costDate')
        models.Profit.objects.create(cost=cost, category=select, date=date)
        return render(request, 'costs.html')
    costList = models.Profit.objects.all()
    return render(request, 'costs.html', {'costList': costList})
