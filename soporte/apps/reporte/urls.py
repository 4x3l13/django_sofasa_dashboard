from rest_framework.routers import DefaultRouter
from .views import ReporteViewSet,ReporteIndex,ReporteInsert,ReporteEdit,ReporteDelete,ReporteDownload
from django.urls import include, path

router = DefaultRouter()
router.register('api',ReporteViewSet)
urlpatterns = [
               path('', ReporteIndex.as_view(),name='reporte_index'),
               path('insert', ReporteInsert.as_view(),name='reporte_insert'),
               path('edit/<int:pk>/', ReporteEdit.as_view(),name='reporte_edit'),
               path('delete/<int:pk>/', ReporteDelete.as_view(),name='reporte_delete'),
               path('download', ReporteDownload.as_view(),name='reporte_download'),
               path('',include(router.urls)),
               ]