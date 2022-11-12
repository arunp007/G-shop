from django.shortcuts import render
from random import random
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from.models import *

def admin_home(request):
    return render(request, 'admin_home.html')

def grocery_add(request):
    if request.method == 'POST':
        name = request.POST['gname']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        file_name = str(random())+image.name
        image.name = file_name
        file_object = FileSystemStorage()
        file_object.save(file_name, image)
        object_details = Grocery(name = name, description = description, price = price, image = image)
        object_details.save()
    return render(request, 'grocery_add.html')

def medicine_add(request):
    if request.method == 'POST':
        name = request.POST['mname']
        description = request.POST['mdescription']
        price = request.POST['mprice']
        image = request.FILES['image']
        file_name = str(random())+image.name
        image.name = file_name
        file_object = FileSystemStorage()
        file_object.save(file_name, image)
        object_details = Medicine(name = name, description = description, price = price, image = image)
        object_details.save()
    return render(request, 'medicine_add.html')