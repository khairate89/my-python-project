from django.contrib import admin
from django.urls import path
from employee_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:emp_id>/', views.update_employee, name='update_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
]
# employee_project/urls.py

from django.urls import path
from employee_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:emp_id>/', views.update_employee, name='update_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('delete_file/<str:filename>/', views.delete_uploaded_file, name='delete_file'),
]
