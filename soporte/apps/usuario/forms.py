from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class InsertForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',]
        
        labels = {'username':'Usuario',
                  'first_name':'Nombre',
                  'last_name' :'Apellido',
                  'email': 'Correo',}
        
        widgets = {'username': forms.TextInput(attrs={'class':'form-control','autocomplete' : 'off', 'required':"",'autofocus':""}),
                  'first_name': forms.TextInput(attrs={'class':'form-control','autocomplete' : 'nope', 'required':""}),
                  'last_name' : forms.TextInput(attrs={'class':'form-control','autocomplete' : 'nope', 'required':""}),
                  'email': forms.EmailInput(attrs={'class':'form-control','autocomplete' : 'nope', 'required':""}),}