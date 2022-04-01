from django.urls import path
from apps.encuesta.views import encuestaIndex,EncuestaChart,EncuestaDownload,EncuestaSearch

urlpatterns = [
    path('', encuestaIndex,name='encuesta_index'),
    path('search', EncuestaSearch.as_view(),name='encuesta_search'),
    path('chart', EncuestaChart.as_view(),name='encuesta_chart'),
    path('download', EncuestaDownload.as_view(),name='encuesta_download'),   
]