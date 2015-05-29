# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from . import user_orm_label, user_model_label, user_model_data


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Poll.user'
        db.add_column(u'poll_poll', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Poll.user'
        db.delete_column(u'poll_poll', 'user_id')


    models = {
        u'poll.item': {
            'Meta': {'ordering': "['pos']", 'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Poll']"}),
            'pos': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'poll.poll': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Poll'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s']" % user_orm_label, 'null': 'True', 'blank': 'True'})
        },
        u'poll.vote': {
            'Meta': {'object_name': 'Vote'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Item']"}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Poll']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'uservote'", 'null': 'True', 'to': u"orm['%s']" % user_orm_label})
        },
        user_model_label: user_model_data
    }

    complete_apps = ['poll']