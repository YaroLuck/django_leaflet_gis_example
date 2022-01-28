from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from app.models import ExampleGeoModel


class ExampleDetailView(DetailView):
    model = ExampleGeoModel
    template_name = 'app/example_template.html'
    context_object_name = 'example_geo_model'
