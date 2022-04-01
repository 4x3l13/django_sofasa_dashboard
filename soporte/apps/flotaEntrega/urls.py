from django.urls import path
from apps.flotaEntrega.views import insert,FlotaEntregaList,FlotaEntregaExport,FlotaEntregaReportView,FlotaEntregaReportDownload,FlotaEntregaChart

urlpatterns = [
    path('', FlotaEntregaList.as_view(),name='flotaEntrega_index'),
    path('insert',insert, name= 'flotaEntrega_insert'),
    path('export', FlotaEntregaExport.as_view(),name='flotaEntrega_export'),
    path('reportView', FlotaEntregaReportView.as_view(),name='flotaEntrega_reportView'),
    path('reportDownload', FlotaEntregaReportDownload.as_view(),name='flotaEntrega_reportDownload'),
    path('chart', FlotaEntregaChart.as_view(),name='flotaEntrega_chart'),
]