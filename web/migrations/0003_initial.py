# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Choice'
        db.create_table(u'web_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lang', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'web', ['Choice'])

        # Adding model 'Poll'
        db.create_table(u'web_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Choice'])),
            ('content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('lang', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'web', ['Poll'])


    def backwards(self, orm):
        # Deleting model 'Choice'
        db.delete_table(u'web_choice')

        # Deleting model 'Poll'
        db.delete_table(u'web_poll')


    models = {
        u'web.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'web.poll': {
            'Meta': {'object_name': 'Poll'},
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Choice']"}),
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']