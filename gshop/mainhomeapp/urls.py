from django.urls import path
from.import views

urlpatterns = [
    path('main_home', views.main_home, name = 'main_home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('admin_signup', views.admin_signup),
    path('user_signup', views.user_signup, name = 'user_signup'),
]