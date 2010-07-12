# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'TwitterStatus.pub_date'
        db.alter_column('common_twitterstatus', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'TwitterStatus.pub_date'
        db.alter_column('common_twitterstatus', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'common.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'common.twitterstatus': {
            'Meta': {'object_name': 'TwitterStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pickle_zip': ('django.db.models.fields.TextField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['common']
