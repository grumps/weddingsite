__author__ = 'Max Resnick'
from django.conf.urls import patterns, url
from playlistform import views

urlpatterns = patterns('',

                       url(r'^$', views.playListAdd, name='playlist'),
                       )
