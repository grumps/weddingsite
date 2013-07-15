from django.db import models
from django.forms import ModelForm

# Create your models here.

class Submitter(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_added = models.DateField()


class SubmittedArtist(models.Model):
    artist = models.CharField()
    artist_id = models.CharField()


class SubmittedSongs(models.Model):
    artist = models.ForeignKey(SubmittedArtist)
    songs = models.CharField
    songs_ids = models.CharField()


class SubmitterForm(ModelForm):
    class Meta:
        model = Submitter
        exclude = ('date_added',)

class ArtistForm (ModelForm):
    class Meta:
        model = SubmittedArtist


class SubmittedSongs(ModelForm):
    class Meta:
        model = SubmittedArtist