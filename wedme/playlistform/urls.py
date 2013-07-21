__author__ = 'Max Resnick'
from django.conf.urls import patterns, url
from wedme.playlistform import views

urlpatterns = patterns('',

                       url(r'^$', views.playlistAdd, name='playlist'),
                       )
