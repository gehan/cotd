from django.conf import settings

def base_settings(request):

    server_base       = settings.SERVER_BASE
    media_url         = settings.MEDIA_URL
    fb_app_id         = settings.FACEBOOK_APP_ID
        
    return locals()
