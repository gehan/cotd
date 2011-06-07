from django.conf import settings
from django.shortcuts import render_to_response 
from django.template import RequestContext

from cotd.models import * 

def home(request):
    d = {'cotd': COTD.get_cotd()}
    return render_to_response("index.html", d, context_instance=RequestContext(request))

def token(request):
    return render_to_response("token.html", {}, context_instance=RequestContext(request))