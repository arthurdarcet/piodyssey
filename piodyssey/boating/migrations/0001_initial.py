# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('boating_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('boating', ['Category'])

        # Adding model 'Question'
        db.create_table('boating_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('_responseA', self.gf('django.db.models.fields.TextField')(null=True)),
            ('_responseB', self.gf('django.db.models.fields.TextField')(null=True)),
            ('_responseC', self.gf('django.db.models.fields.TextField')(null=True)),
            ('_responseD', self.gf('django.db.models.fields.TextField')(null=True)),
            ('solution', self.gf('django.db.models.fields.CharField')(max_length=4, null=True)),
            ('explanation', self.gf('django.db.models.fields.TextField')(null=True)),
            ('explanation_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['boating.Category'], null=True)),
            ('scraper', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('boating', ['Question'])

        # Adding unique constraint on 'Question', fields ['slug', 'scraper']
        db.create_unique('boating_question', ['slug', 'scraper'])

        # Adding model 'Session'
        db.create_table('boating_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('boating', ['Session'])

        # Adding model 'Answer'
        db.create_table('boating_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['boating.Question'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['boating.Session'])),
        ))
        db.send_create_signal('boating', ['Answer'])


    def backwards(self, orm):
        # Removing unique constraint on 'Question', fields ['slug', 'scraper']
        db.delete_unique('boating_question', ['slug', 'scraper'])

        # Deleting model 'Category'
        db.delete_table('boating_category')

        # Deleting model 'Question'
        db.delete_table('boating_question')

        # Deleting model 'Session'
        db.delete_table('boating_session')

        # Deleting model 'Answer'
        db.delete_table('boating_answer')


    models = {
        'boating.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boating.Question']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': "orm['boating.Session']"})
        },
        'boating.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'boating.question': {
            'Meta': {'unique_together': "(('slug', 'scraper'),)", 'object_name': 'Question'},
            '_responseA': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_responseB': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_responseC': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_responseD': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boating.Category']", 'null': 'True'}),
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
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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