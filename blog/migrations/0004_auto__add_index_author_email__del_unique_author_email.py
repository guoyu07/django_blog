# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Author', fields ['email']
        #db.delete_unique('authors', ['email'])

        # Adding index on 'Author', fields ['email']
        db.create_index('authors', ['email'])


    def backwards(self, orm):
        # Removing index on 'Author', fields ['email']
        db.delete_index('authors', ['email'])

        # Adding unique constraint on 'Author', fields ['email']
        db.create_unique('authors', ['email'])


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article', 'db_table': "'articles'"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Author']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'blog.author': {
            'Meta': {'object_name': 'Author', 'db_table': "'authors'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment', 'db_table': "'comments'"},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Article']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Author']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']