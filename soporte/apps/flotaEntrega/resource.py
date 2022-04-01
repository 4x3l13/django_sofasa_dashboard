from import_export import resources
from apps.flotaEntrega.models import FlotaEntrega

class FlotaEntregaResource(resources.ModelResource):
    class Meta:
        model = FlotaEntrega