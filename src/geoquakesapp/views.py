from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from django.template.context import Context
from geoquakesapp.models   import Quake , Quake_Predections
import pandas as pd


# Create your views here.
def quake_dataset(request):
    quakes = serialize('json',Quake.objects.order_by("ID")[:1400])
    return HttpResponse(quakes , content_type="json")

def quake_dataset_pred(request):
    quakes_pred = serialize('json',Quake_Predections.objects.all()[:1400])
    return HttpResponse(quakes_pred , content_type="json")


def quake_dataset_pred_risk (request):
    quakes_risk = serialize('json',Quake_Predections.objects.filter(Magnitude__gt=6.5))
    return HttpResponse(quakes_risk, content_type="json")

def home (request):
    return render(
        request,
        "app/index.html",
        {
            'title':'Home page'
        }
    )
 