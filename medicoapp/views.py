from django.shortcuts import render, redirect
from medicoapp.models import Company, Patient, Appointment,Member
from medicoapp.forms import AppointmentForm



# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'] ).exists():
                member= Member.objects.get(username=request.POST['username'],
                                           password=request.POST['password'],
                                          )
                return render(request,'index.html',{'member':member})
        else:
            return render(request, 'login.html')
    else:
     return render(request, 'login.html')



def start(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        contacts = Company(name=request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
                           staff=request.POST['staff'])
        contacts.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')


def patient(request):
    if request.method == 'POST':
        patients = Patient(fullname=request.POST['fullname'],
                           email=request.POST['email'],
                           medicalhistory=request.POST['medicalhistory'],
                           age=request.POST['age'])
        patients.save()
        return redirect('/patient')
    else:
        return render(request, 'patient.html')


def Appoint(request):
    if request.method == 'POST':
        appointment = Appointment(name=request.POST['name'],
                                  email=request.POST['email'],
                                  phone=request.POST['phone'],
                                  date=request.POST['date'],
                                  department=request.POST['department'],
                                  doctor=request.POST['doctor'],
                                  message=request.POST['message'])

        appointment.save()
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')

#fetching data
def show(request):
    data = Appointment.objects.all()
    return render(request, 'show.html', {'appointment': data})

#deleting data
def delete(request,id):
    myappointment=Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('show')

def edit(request,id):
    appointment = Appointment.objects.get(id=id)
    return render(request,'edit.html',{'x':appointment})

def update(request,id):
    appointment = Appointment.objects.all(id=id)
    form = AppointmentForm (request.POST,instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')


def register(request):
     if request.method == 'POST':
         members = Member(
             name = request.POST['name'],
             username = request.POST['username'],
             password = request.POST['password'],
        )
         members .save()
         return redirect('/login')
     else:
         return render(request, 'register.html')


def login(request):
    return render(request,'login.html')