from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render_to_response 
from django.template.context import RequestContext
from django.http import HttpResponse
import json

from backend.models import *
# Create your views here.


def render_template(template, request, **kwargs):
  kwargs['template_name'] = template
  return render_to_response(template, kwargs, context_instance=RequestContext(request))

class GalleryView(View):
  def get(self, request):
    qs = Artwork.objects.all()
    data = serializers.serialize("json",qs);
    #return render_template("backend/gallery/json.html", request, data=qs.values())
    return HttpResponse(data, content_type="application/json")