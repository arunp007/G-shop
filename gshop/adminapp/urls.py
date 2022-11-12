from django.urls import path
from.import views

urlpatterns = [ 
    path('admin_home', views.admin_home, name = 'admin_home'),
    path('grocery_add', views.grocery_add, name = 'grocery_add'),
    path('medicine_add', views.medicine_add, name = 'medicine_add'),
]