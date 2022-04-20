from rest_framework import serializers
from .models import Reporte

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ('id','name','description','stored_procedure','parameters')