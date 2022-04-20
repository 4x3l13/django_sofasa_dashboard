from .models import Reporte
from django import forms

class InsertForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['name',
                  'description',
                  'stored_procedure',
                  'parameters',]
        
        labels = {'name':'Nombre',
                  'description':'Descripción',
                  'stored_procedure' :'Procedimiento Almacenado',
                  'parameters': 'Parametros',}
        
        widgets = {'name': forms.TextInput(attrs={'class':'form-control','autocomplete' : 'nope', 'required':"",'autofocus':""}),
                  'description': forms.Textarea(attrs={'class':'form-control','autocomplete' : 'nope', 'required':"","rows":"4"}),
                  'stored_procedure' : forms.TextInput(attrs={'class':'form-control','autocomplete' : 'nope', 'required':""}),
                  'parameters': forms.Textarea(attrs={'class':'form-control','autocomplete' : 'nope',"rows":"4"}),}