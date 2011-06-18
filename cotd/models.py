from django.db import models
from datetime import date
import facegraph
from model_fields import DataField
from picklefield import PickledObjectField
import random

class COTD(models.Model):
    date = models.DateField(unique=True)
    captain = models.ForeignKey('Captain')
    photo = models.ForeignKey('Photo', null=True)

    def __unicode__(self):
        return "id=%s, date=%s, captain=%s" % (self.pk, self.date, self.captain)

    @classmethod
    def get_cotd(cls, dte=None):
        if dte is None:
            dte = date.today()
        try:
            cotd = cls.objects.get(date=dte)
        except cls.DoesNotExist:
            cotd = cls.objects.create(date=dte, captain=Captain.get_random_captain())
        return cotd
    
    def get_photo(self):
        if not self.photo:
            self.photo = self.captain.get_random_photo()
            self.save()
        tag_x, tag_y = self.photo.get_tag(self.captain.fbid)
        return self.photo, tag_x, tag_y

class Captain(models.Model):
    name = models.CharField(max_length=255)
    fbid = models.CharField(max_length=255)

    def __unicode__(self):
        return "id=%s, name=%s, fbid=%s" % (self.pk, self.name, self.fbid)
    
    @classmethod
    def get_random_captain(cls):
        total = cls.objects.count()
        idx = random.randrange(0, total) + 1
        return cls.objects.get(pk=idx)
    
    def get_random_photo(self):
        access_token = Config.objects.get().access_token
        graph = facegraph.Graph(access_token)
        photos_node = graph[self.fbid].photos | ('fields', 'id, source,tags') | ('limit', 500)
        response = photos_node().as_dict()
        photos = response.get('data')
        n = 0
        while True and n < 10000:
            n += 1
            photo_idx = random.randrange(0, len(photos))
            photo = photos[photo_idx]
            if photo.get('tags') and len(photo.get('tags')) > 1:
                continue
            defaults = {'url': photo.get('source')}
            (photo_obj, created) = Photo.objects.get_or_create(pid=photo.get('id'), defaults=defaults)
            if created:
                photo_obj.data.tags = photo.get('tags').get('data')
                photo_obj.save()
                break
        return photo_obj
    
class Photo(models.Model):
    pid = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=4096)
    data_field = PickledObjectField(compress=True, default=dict)

    def __unicode__(self):
        return "id=%s, pid=%s, url=%s" % (self.pk, self.pid, self.url)
    
    @property
    def data(self):
        defaults = {}
        return DataField(self, "data_field", defaults)
    
    def get_tag(self, fbid):
        if self.data.tags:
            for tag in self.data.tags:
                if tag.get('id') == str(fbid):
                    return tag.get('x'), tag.get('y')
        return None, None
    
class Config(models.Model):
    access_token = models.CharField(max_length=255)