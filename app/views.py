from django.shortcuts import render, redirect
from .models import Menu, Reservation
from .forms import MenuForm, ReservationForm

# Create your views here.


def home(request):
    menus = Menu.objects.all()
    return render(request, 'pages/home.html', {'menus' : menus})

def menus(request):
    menus = Menu.objects.all()
    context = {
        'menus' : menus
    }
    return render(request, 'pages/menus.html', context)


def menu_detail(request, title):
    return render(request, 'pages/menu_detail.html')


from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            number_of_guests = form.cleaned_data['number_of_guests']

            Reservation.objects.create(full_name=full_name, phone=phone, date=date, time=time, number_of_guests=number_of_guests)
            
    else:
        form = ReservationForm()
    return render(request, 'pages/resevation_page.html', {'form': form})

