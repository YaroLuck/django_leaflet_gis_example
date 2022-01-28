from django.contrib import admin

# Register your models here.
from django.contrib.admin import site
from leaflet.admin import LeafletGeoAdmin

from app.models import ExampleGeoModel

site.register(ExampleGeoModel, LeafletGeoAdmin)
