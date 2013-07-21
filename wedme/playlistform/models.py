from django.db import models
from django.forms import ModelForm


class Submitter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()


class Artist(models.Model):
    artist = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    song = models.CharField(max_length=200)
    songs_id = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)


class SubmitterForm(ModelForm):
    class Meta:
        model = Submitter


class ArtistForm(ModelForm):
    class Meta:
        model = Artist


class SongForm(ModelForm):
    class Meta:
        model = Song
