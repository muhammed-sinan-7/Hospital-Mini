from django.shortcuts import render
from . models import Doctors,Department
# Create your views here.
def home(request):
    return render(request,'Home.html')

def department(request):
    departments = Department.objects.all()
    print(departments)
    return render(request,'Department.html',{"departments":departments})

def appointment(request):
    return render(request,'Appointment.html')

def doctors(request):
    doctors = Doctors.objects.all()
    return render(request,'Doctors.html',{'doctors':doctors})

def contact(request):
    return render(request,'Contact.html')

