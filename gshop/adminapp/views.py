from django.shortcuts import render
from django.http import HttpResponse

def admin_home(request):
    return render(request, 'admin_home.html')

def product_add(request):
    return render(request, 'product_add.html')
