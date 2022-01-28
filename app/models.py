from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class ExampleGeoModel(models.Model):
    """ Тестовая модель с геоданными """

    location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)

    line = gis_models.LineStringField(blank=True, null=True)

