from django.shortcuts import render
from . models import Doctors,Department
# Create your views here.
def home(request):
    visits = int(request.COOKIES.get('visits',0))
    visits = visits+1
    response=render(request,'Home.html',{'visits':visits})
    response.set_cookie('visits',visits)
    return response

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

