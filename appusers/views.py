from django.shortcuts import render, redirect
app_name="appusers"
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.


def index(request):
    menus = Menu.objects.all()
    data = {'menus':menus}
    return render(request, 'index.html', data)
    
def menu(request):
    menus = Menu.objects.all()
    data = {'menus':menus}
    return render(request, 'menu.html', data)

def about(request):
    menus = Menu.objects.all()
    data = {'menus':menus}
    return render(request, 'about.html', data)

def gallery(request):
    gallerys = Gallery.objects.all()
    data = {'gallerys':gallerys}
    return render(request, 'gallery.html', data)
    
def reservation(request):
    form = ReservationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            a = (request.POST['name'])
            b = (request.POST['email'])
            c = (request.POST['phone_number'])
            d = (request.POST['num_persons'])
            e = (request.POST['reservation_datetime'])
            g = Reserve(name=a,email=b,phone_number=c,num_persons=d,reservation_datetime=e)
            g.save()
            return redirect('/')
    data= {'forms':form,}
    return render(request, 'reservation.html', data)
    
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            a = (request.POST['name'])
            b = (request.POST['email'])
            c = (request.POST['phone_number'])
            d = (request.POST['message'])
            g = Contact(name=a,email=b,phone_number=c,message=d)
            g.save()
            return redirect('/')
    data= {'forms':form,}
    return render(request, 'contact.html', data)
