from django.urls import path
from apps.encuesta.views import encuestaIndex,EncuestaChart,EncuestaDownload,EncuestaSearchAPI#,EncuestaSearch

urlpatterns = [
    path('', encuestaIndex,name='encuesta_index'),
    #path('search', EncuestaSearch.as_view(),name='encuesta_search'),
    path('search', EncuestaSearchAPI.as_view(),name='encuesta_search'),
    path('chart', EncuestaChart.as_view(),name='encuesta_chart'),
    path('download', EncuestaDownload.as_view(),name='encuesta_download'),   
]