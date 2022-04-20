from django.db import models

class Reporte(models.Model):
    name = models.CharField(max_length= 100)
    description =  models.CharField(max_length= 500)
    stored_procedure =  models.CharField(max_length= 200)
    parameters = models.CharField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        permissions = (('graph_reporte', 'Can graph reporte'),
                       ('download_reporte', 'Can download reporte'),)
    
#CREATE / INSERT - ADD / POST
#RETRIEVE / FETCH / GET
#UPDATE / EDIT / PUT
#DELETE / REMOVE / DELETE