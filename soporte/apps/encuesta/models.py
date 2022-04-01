from django.db import models

# Create your models here.
class Encuesta(models.Model):

    class Meta:
        permissions = (('graph_encuesta', 'Can graph encuesta'),
                       ('download_encuesta', 'Can download encuesta'),
                       ('search_encuesta', 'Can search encuesta'))