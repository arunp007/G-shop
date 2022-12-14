from django.shortcuts import render , redirect
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

def contact_table(request):
    contact_data = Contact.objects.all()
    return render(request, 'contact_table.html', {'contact' : contact_data})

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

def delete(request,id):
    User.objects.get(id=id).delete()
    return redirect('user_table')

def update(request,id):
    update_data = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        User.objects.filter(id = id).update(name = name, email = email, phone = phone, address = address, password = password)
        return redirect('user_table')

    else:
    
        update_data = User.objects.get(id = id)
    return render(request, 'signup_user.html', {'update': update_data})

def user_table(request):
    user_data = User.objects.all()
    return render(request, 'user_table.html', {'user': user_data})

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            current_user = Admin.objects.get(email = email, password = password)
            request.session['xyz'] = current_user.id
            return redirect('admin_home')

        except Admin.DoesNotExist:
            return render(request, 'login_admin.html', {'message': "Username And Password Is Wrong"})
    return render(request, 'login_admin.html')

def admin_logout(request):
    request.session.flush()
    return render(request, 'login_admin.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            current_user = User.objects.get(email = email, password = password)
            request.session['xyz'] = current_user.id
            return redirect('user_home')

        except User.DoesNotExist:
            return render(request, 'login_user.html', {'message': "Username And Password Is Wrong"})
    return render(request, 'login_user.html')

def user_logout(request):
    request.session.flush()
    return render(request, 'login_user.html')

def error(request):
    return render(request, 'error.html')