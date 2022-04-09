from rest_framework import serializers
#from .models import EncuestasBuscarVin

class EncuestaBuscarVinSerializer(serializers.Serializer):
    #class meta:
        #model = EncuestasBuscarVin
        #fields = ('vin','placa')
    vin = serializers.CharField()
    placa = serializers.CharField()