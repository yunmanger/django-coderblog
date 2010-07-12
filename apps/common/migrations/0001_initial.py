# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('common_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('common', ['Link'])

        # Adding model 'TwitterStatus'
        db.create_table('common_twitterstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('pickle_zip', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('common', ['TwitterStatus'])


    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('common_link')

        # Deleting model 'TwitterStatus'
        db.delete_table('common_twitterstatus')


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
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['common']
