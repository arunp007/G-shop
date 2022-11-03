from django.shortcuts import render
from django.http import HttpResponse

def main_home(request):
    return render(request, 'main_home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')