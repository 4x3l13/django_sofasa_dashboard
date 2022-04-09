from django.urls import include, path
from rest_framework import routers
from .views import EncuestaBuscarVinViewSet

#router = routers.DefaultRouter()
#router.register(r'encuestasBuscarVin', views.EncuestaBuscarVinViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path('apiEncuestaBuscarVin/', EncuestaBuscarVinViewSet.as_view(),name='apiEncuestaBuscarVin')
]