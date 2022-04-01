from django.urls import path
from apps.usuario.views import UsuarioInsert, UsuarioIndex

urlpatterns = [
    path('',UsuarioIndex.as_view(), name= 'usuario_index'),
    path('insert',UsuarioInsert.as_view(), name= 'usuario_insert'),
]