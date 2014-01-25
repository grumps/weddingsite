# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SecondPartner'
        db.delete_table(u'rsvp_wedding_secondpartner')

        # Adding model 'PartnerGuest'
        db.create_table(u'rsvp_wedding_partnerguest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('will_arrive_thursday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('will_stay_saturday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('will_attend', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_vegetarian', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='NULL', max_length=140)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='NULL', max_length=140)),
            ('primaryguest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp_wedding.PrimaryGuest'])),
        ))
        db.send_create_signal(u'rsvp_wedding', ['PartnerGuest'])


    def backwards(self, orm):
        # Adding model 'SecondPartner'
        db.create_table(u'rsvp_wedding_secondpartner', (
            ('last_name', self.gf('django.db.models.fields.CharField')(default='NULL', max_length=140)),
            ('will_stay_saturday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(related_name='guest_primary', unique=True, to=orm['rsvp_wedding.PrimaryGuest'])),
            ('will_attend', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_vegetarian', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='NULL', max_length=140)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('will_arrive_thursday', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'rsvp_wedding', ['SecondPartner'])

        # Deleting model 'PartnerGuest'
        db.delete_table(u'rsvp_wedding_partnerguest')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rsvp_wedding.partnerguest': {
            'Meta': {'object_name': 'PartnerGuest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "'NULL'", 'max_length': '140'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'primaryguest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp_wedding.PrimaryGuest']"}),
            'will_arrive_thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'will_attend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'will_stay_saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rsvp_wedding.primaryguest': {
            'Meta': {'object_name': 'PrimaryGuest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_allowed_partner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'will_arrive_thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'will_attend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'will_stay_saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['rsvp_wedding']