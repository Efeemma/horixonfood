from django import forms
from .models import *

class ReservationForm(forms.ModelForm):
    NUM_PERSONS_CHOICES = [(1, '1 Person'), (2, '2 Persons'), (3, '3 Persons'), (4, '4 Persons'), (5, '5 Persons'), (6, '6 Persons'), (7, '7 Persons'), (8, '8 Persons')]

    num_persons = forms.TypedChoiceField(
        choices=NUM_PERSONS_CHOICES,
        coerce=int,  # Ensure the selected value is an integer
        widget=forms.Select(attrs={'class': 'form-control'}),  # Add a CSS class
    )
    reservation_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimepicker'}),
        input_formats=['%Y-%m-%d %H:%M:%S']
    )
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    phone_number = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    email = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    reservation_datetime = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    
    class Meta:
        model = Reserve
        fields = ['name','email', 'num_persons', 'phone_number', 'reservation_datetime']
        
        
     
class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    phone_number = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    email = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    message = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    class Meta:
        model = Reserve
        fields = ['name','email','phone_number', 'message']