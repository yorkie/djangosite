# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'web_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lang', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'web', ['Category'])

        # Adding model 'Article'
        db.create_table(u'web_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Category'])),
            ('content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('lang', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'web', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'web_category')

        # Deleting model 'Article'
        db.delete_table(u'web_article')


    models = {
        u'web.article': {
            'Meta': {'object_name': 'Article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Category']"}),
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'web.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']