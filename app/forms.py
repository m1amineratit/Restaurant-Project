from django import forms
from .models import Menu, Reservation


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('full_name', 'phone', 'date', 'time', 'number_of_guests', )