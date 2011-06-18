# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'COTD'
        db.create_table('cotd_cotd', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(unique=True)),
            ('captain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cotd.Captain'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cotd.Photo'], null=True)),
        ))
        db.send_create_signal('cotd', ['COTD'])

        # Adding model 'Captain'
        db.create_table('cotd_captain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fbid', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('cotd', ['Captain'])

        # Adding model 'Photo'
        db.create_table('cotd_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=4096)),
        ))
        db.send_create_signal('cotd', ['Photo'])

        # Adding model 'Config'
        db.create_table('cotd_config', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('cotd', ['Config'])


    def backwards(self, orm):
        
        # Deleting model 'COTD'
        db.delete_table('cotd_cotd')

        # Deleting model 'Captain'
        db.delete_table('cotd_captain')

        # Deleting model 'Photo'
        db.delete_table('cotd_photo')

        # Deleting model 'Config'
        db.delete_table('cotd_config')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        }
    }

    complete_apps = ['cotd']
