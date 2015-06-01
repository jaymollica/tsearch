from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render_to_response 
from django.template.context import RequestContext
from django.http import HttpResponse
from django.http import HttpRequest
import json

from backend.models import *
# Create your views here.

def render_template(template, request, **kwargs):
  kwargs['template_name'] = template
  return render_to_response(template, kwargs, context_instance=RequestContext(request))

class GalleryView(View):
  def get(self, request):
    my_filters = request.GET.get('filters')
    decade = request.GET.get('decade')

    country = request.GET.get('country')
    country_obj = Country.objects.filter(name=country)
    country_id = country_obj[0].id

    medium_keyword = request.GET.get('medium')
    medium_list = Medium.objects.filter(medium__contains=medium_keyword)

    qs = Artwork.objects.filter(country=country_id, 
                                date_created__range=["19"+decade+"0-01-01", "19"+decade+"9-12-31"], 
                                medium__in=medium_list).order_by('?')[:20]
    #qs_data = Artwork.objects.filter(Country="Mexico")
    data = serializers.serialize("json",qs)
    #return render_template("backend/gallery/json.html", request, data=qs.values())
    return HttpResponse(data, content_type="application/json")


class HomeView(View):
  def get(self, request):
    return render_template("backend/index.html", request)