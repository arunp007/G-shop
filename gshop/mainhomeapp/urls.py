from django.urls import path
from.import views

urlpatterns = [
    path('main_home', views.main_home, name = 'main_home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('contact_table', views.contact_table, name = 'contact_table'),
    path('admin_signup', views.admin_signup, name = 'admin_signup'),
    path('user_signup', views.user_signup, name = 'user_signup'),
    path('user_table', views.user_table, name = 'user_table'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('admin_login', views.admin_login, name = 'admin_login'),
    path('user_login', views.user_login, name = 'user_login'),

]