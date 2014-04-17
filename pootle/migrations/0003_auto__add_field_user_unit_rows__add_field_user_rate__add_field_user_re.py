# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.unit_rows'
        db.add_column(u'pootle_user', 'unit_rows',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=9),
                      keep_default=False)

        # Adding field 'User.rate'
        db.add_column(u'pootle_user', 'rate',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'User.review_rate'
        db.add_column(u'pootle_user', 'review_rate',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'User.score'
        db.add_column(u'pootle_user', 'score',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding M2M table for field alt_src_langs on 'User'
        m2m_table_name = db.shorten_name(u'pootle_user_alt_src_langs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm['pootle.user'], null=False)),
            ('language', models.ForeignKey(orm[u'pootle_language.language'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'language_id'])


    def backwards(self, orm):
        # Deleting field 'User.unit_rows'
        db.delete_column(u'pootle_user', 'unit_rows')

        # Deleting field 'User.rate'
        db.delete_column(u'pootle_user', 'rate')

        # Deleting field 'User.review_rate'
        db.delete_column(u'pootle_user', 'review_rate')

        # Deleting field 'User.score'
        db.delete_column(u'pootle_user', 'score')

        # Removing M2M table for field alt_src_langs on 'User'
        db.delete_table(db.shorten_name(u'pootle_user_alt_src_langs'))


    models = {
        'pootle.user': {
            'Meta': {'object_name': 'User'},
            'alt_src_langs': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'to': u"orm['pootle_language.Language']", 'symmetrical': 'False', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'review_rate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'unit_rows': ('django.db.models.fields.SmallIntegerField', [], {'default': '9'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'pootle_app.directory': {
            'Meta': {'ordering': "['name']", 'object_name': 'Directory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child_dirs'", 'null': 'True', 'to': "orm['pootle_app.Directory']"}),
            'pootle_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'pootle_language.language': {
            'Meta': {'ordering': "['code']", 'object_name': 'Language', 'db_table': "'pootle_app_language'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'directory': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pootle_app.Directory']", 'unique': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nplurals': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'pluralequation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specialchars': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['pootle']