from cotd.models import *

def setup():
    Captain.objects.create(name="Sam", fbid="502605077")
    Captain.objects.create(name="Taryn", fbid="670923540")
    Captain.objects.create(name="Gehan", fbid="502531952")
    Captain.objects.create(name="Tim", fbid="51039793")
    Config.objects.create(access_token="103428196417085|2ec9f49255d67724228d4c3e.1-502531952|mcnFVD514urhHcbxAzyKLusaFS4")