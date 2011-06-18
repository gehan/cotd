from django.conf import settings
from django.shortcuts import render_to_response 
from django.template import RequestContext

from cotd.models import * 

def home(request):
    cotd = COTD.get_cotd()
    (photo, tag_x, tag_y) = cotd.get_photo()
    d = {'cotd': cotd,
         'photo': photo,
         'tag': {'x': tag_x or 'null',
                 'y': tag_y or 'null'}}
    return render_to_response("index.html", d, context_instance=RequestContext(request))

def token(request):
    return render_to_response("token.html", {}, context_instance=RequestContext(request))