from django.urls import path
from.import views

urlpatterns = [ 
    path('admin_home', views.admin_home, name = 'admin_home'),
    path('grocery_add', views.grocery_add, name = 'grocery_add'),
    path('grocery_table', views.grocery_table, name = 'grocery_table'),
    path('grocery_update/<int:id>', views.grocery_update, name = 'grocery_update'),
    path('grocery_delete/<int:id>', views.grocery_delete, name = 'grocery_delete'),
    path('medicine_add', views.medicine_add, name = 'medicine_add'),
    path('medicine_table', views.medicine_table, name = 'medicine_table'),
    path('medicine_delete/<int:id>', views.medicine_delete, name = 'medicine_delete'),
    path('medicine_update/<int:id>', views.medicine_update, name = 'medicine_update'),
    path('grocery', views.grocery, name = 'grocery'),
    path('medicine', views.medicine, name = 'medicine'),
]