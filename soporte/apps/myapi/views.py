from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EncuestaBuscarVinSerializer

class EncuestaBuscarVinViewSet (APIView):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute('select * from flotaEntrega_flotaentrega where vin = %s',[request.GET.get('vin')])
        columns = [column[0] for column in cursor.description]
        rows = []
        for row in cursor.fetchall():
            rows.append(dict(zip(columns,row)))
        cursor.close()
        results = EncuestaBuscarVinSerializer(rows,many=True).data
        return Response(results)