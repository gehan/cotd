from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cotd.views',
    (r'^$',      'home'),
    (r'^token$', 'token'),
    
    (r'^admin/', include(admin.site.urls)),
    
)

# For local media
if getattr(settings, 'IS_LOCAL', False):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,
                                                                               'show_indexes': True}),
    )