from django.shortcuts import render, redirect
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

def grocery_table(request):
    grocery_data = Grocery.objects.all()
    return render(request, 'grocery_table.html', {'grocery': grocery_data})

def grocery_update(request,id):
    update_data = ""
    if request.method == 'POST':
       name = request.POST['gname']
       description = request.POST['description']
       price = request.POST['price']
       Grocery.objects.filter(id=id).update(name = name, description = description, price = price)
       return redirect('grocery_table')

    else:
        update_data = Grocery.objects.get(id=id)
        return render(request, 'grocery_add.html', {'update': update_data})
    return render(request, 'grocery_add.html')

def grocery_delete(request,id):
    Grocery.objects.get(id=id).delete()
    return redirect('grocery_table')

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

def medicine_table(request):
    medicine_data = Medicine.objects.all()
    return render(request, 'medicine_table.html',{'medicine': medicine_data})

def medicine_delete(request,id):
    Medicine.objects.get(id=id).delete()
    return redirect('medicine_table')

def medicine_update(request,id):
    update_data = ""
    if request.method == 'POST':
        name = request.POST['mname']
        description = request.POST['mdescription']
        price = request.POST['mprice']
        Medicine.objects.filter(id=id).update(name = name, description = description, price = price)
        return redirect('medicine_table')

    else:
        update_data = Medicine.objects.get(id=id)
        return render(request, 'medicine_add.html', {'update': update_data})
    return render(request, 'medicine_add.html')

def grocery(request):
    grocery_data = Grocery.objects.all()
    return render(request, 'grocery.html', {'grocery': grocery_data})

def medicine(request):
    medicine_data = Medicine.objects.all()
    return render(request, 'medicine.html', {'medicine': medicine_data})