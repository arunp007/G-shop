from django.urls import path
from.import views

urlpatterns = [
    path('main_home', views.main_home, name = 'main_home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
]