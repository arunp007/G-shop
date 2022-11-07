from django.urls import path
from.import views

urlpatterns = [
    path('main_home', views.main_home, name = 'main_home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('admin_signup', views.admin_signup, name = 'admin_signup'),
    path('user_signup', views.user_signup, name = 'user_signup'),
    path('admin_login', views.admin_login, name = 'admin_login'),
    path('user_login', views.user_login, name = 'user_login'),

]