from django.shortcuts import render
from django.http import HttpResponse
from.models import *

def main_home(request):
    return render(request, 'main_home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact_data = Contact(name = name, email = email, phone = phone, message = message)
        contact_data.save()
    return render(request, 'contact.html')

def admin_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        admin_data = Admin(email = email, password = password)
        admin_data.save()
    return render(request, 'signup_admin.html')

def user_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        user_data = User(name = name, email = email, phone = phone, address = address, password = password)
        user_data.save()
    return render(request, 'signup_user.html')