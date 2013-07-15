from django.db import models
from django import forms

# Create your models here.


class AddToPlaylist(forms.Form):
    submitter_first_name = forms.CharField(max_length=100, required=True)
    submitter_last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    artist = forms.CharField(required=True)
    artist_id = forms.CharField()
    songs = forms.CharField(required=True)
    songs_ids = forms.CharField()