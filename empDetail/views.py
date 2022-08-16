import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # print(request.user)
    emp =Employee.objects.all()[:5]
    return render(request, 'empDetail/index.html',{ 'emp' : emp})

def empLists(request):
    emp =Employee.objects.all()
    return render(request, 'empDetail/empLists.html',{ 'emp' : emp})

@login_required
def detail(request,pk):
    emp = Employee.objects.get(pk = pk)
    return render(request, 'empDetail/detail.html', {'emp' : emp})

@login_required
def delete(request, pk):
    emp = Employee.objects.get(pk = pk)
    emp.delete()
    return empLists(request)

@login_required
def update(request,pk):

    if request.method == "GET":
        empForm = EmployeeForm(instance=Employee.objects.get(pk = pk))
         
    if request.method == "POST":
        empForm = EmployeeForm(request.POST, instance=Employee.objects.get(pk = pk))
        if empForm.is_valid():
            empForm.save()
            return detail(request,pk)
        else:
            return render(request, 'empDetail/update.html', {'empForm' : empForm, 'error' : 'Details are Invalid'})

    return render(request, 'empDetail/update.html', {'empForm' : empForm})


# class EmployeeUpdateView(UpdateView):
#     fields = ['name', 'username', 'email', 'phone','department', 'role']
#     model = Employee



@login_required
def addEmployeeData(request):
    if request.method == 'GET':
        empForm = EmployeeForm()

    if request.method == 'POST':
        empForm = EmployeeForm(request.POST)

        if empForm.is_valid():
            epname = empForm.cleaned_data['name']
            print(epname)
            empForm.save()
            return index(request)

        else:
            return render(request, 'empDetail/addData.html', { 'empForm' : empForm, 'error' :'Details are Invalid' })

        
    return render(request, 'empDetail/addData.html', { 'empForm' : empForm} )


# Authentication Part

