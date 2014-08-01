# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Choice.lang'
        db.alter_column(u'web_choice', 'lang', self.gf('django.db.models.fields.IntegerField')(max_length=10))

        # Changing field 'Poll.lang'
        db.alter_column(u'web_poll', 'lang', self.gf('django.db.models.fields.IntegerField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Choice.lang'
        db.alter_column(u'web_choice', 'lang', self.gf('django.db.models.fields.IntegerField')(max_length=12))

        # Changing field 'Poll.lang'
        db.alter_column(u'web_poll', 'lang', self.gf('django.db.models.fields.IntegerField')(max_length=12))

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