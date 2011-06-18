# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Photo.data_field'
        db.add_column('cotd_photo', 'data_field', self.gf('picklefield.fields.PickledObjectField')(default={}), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Photo.data_field'
        db.delete_column('cotd_photo', 'data_field')


    models = {
        'cotd.captain': {
            'Meta': {'object_name': 'Captain'},
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'cotd.config': {
            'Meta': {'object_name': 'Config'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cotd.cotd': {
            'Meta': {'object_name': 'COTD'},
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotd.Captain']"}),
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotd.Photo']", 'null': 'True'})
        },
        'cotd.photo': {
            'Meta': {'object_name': 'Photo'},
            'data_field': ('picklefield.fields.PickledObjectField', [], {'default': '{}'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        }
    }

    complete_apps = ['cotd']
