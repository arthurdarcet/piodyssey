# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming field 'Session.date' to 'Session.created_at'
        db.rename_column('boating_session', 'date', 'created_at')

        # Adding field 'Session.category'
        db.add_column('boating_session', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['boating.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Renaming field 'Session.created_at' to 'Session.date'
        db.rename_column('boating_session', 'created_at', 'date')

        # Deleting field 'Session.category'
        db.delete_column('boating_session', 'category_id')


    models = {
        'boating.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boating.Question']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boating.Session']", 'related_name': "'answers'"})
        },
        'boating.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'boating.question': {
            'Meta': {'object_name': 'Question', 'unique_together': "(('slug', 'scraper'),)"},
            '_responseA': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_responseB': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_responseC': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_responseD': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['boating.Category']"}),
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'explanation_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'scraper': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'solution': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'})
        },
        'boating.session': {
            'Meta': {'object_name': 'Session'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['boating.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"})
        },
        'users.user': {
            'Meta': {'object_name': 'User'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'parent_email': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'parent_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        }
    }

    complete_apps = ['boating']
