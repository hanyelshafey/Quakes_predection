#from django.db import models
from django.db.models.fields import CharField, DateField

from django.contrib.gis.db import models as GISMODEL

# Create your models here.
class Quake(GISMODEL.Model):
    Date = GISMODEL.CharField(max_length=100)
    latitude = GISMODEL.FloatField()
    longitude = GISMODEL.FloatField()
    Type = GISMODEL.CharField(max_length=100)
    Depth = GISMODEL.FloatField()
    Magnitude = GISMODEL.FloatField()
    Magnitude_type = GISMODEL.CharField(max_length=100)
    ID = GISMODEL.CharField(max_length=100)

    def __str__(self):
        return self.ID

    class Meta:
     
        verbose_name_plural = 'Quake'

class Quake_Predections(GISMODEL.Model):
    latitude = GISMODEL.FloatField()
    longitude = GISMODEL.FloatField()
    Magnitude = GISMODEL.FloatField()
    Depth = GISMODEL.FloatField()
    Score = GISMODEL.FloatField()

    class Meta:
    
        verbose_name_plural = 'Quake_Predections'

