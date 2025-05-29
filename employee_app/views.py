import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        salary = request.POST['salary']
        Employee.objects.create(name=name, department=department, salary=salary)
        return redirect('employee_list')
    return render(request, 'add_employee.html')

def update_employee(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_list')
    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, emp_id):
    Employee.objects.get(id=emp_id).delete()
    return redirect('employee_list')

# upload CSV file
def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return redirect('upload_csv')

        # Save file temporarily (optional)
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        filepath = fs.path(filename)

        # Read and process CSV
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Employee.objects.create(
                    name=row['name'],
                    department=row['department'],
                    salary=row['salary']
                )

        messages.success(request, 'CSV uploaded and data saved.')
        return redirect('employee_list')

    return render(request, 'upload_csv.html')
import os

def delete_uploaded_file(request, filename):
    fs = FileSystemStorage()
    filepath = fs.path(filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        messages.success(request, f'{filename} deleted.')
    else:
        messages.error(request, f'{filename} not found.')
    return redirect('employee_list')
