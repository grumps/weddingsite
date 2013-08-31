from django.db import models
from django.forms import ModelForm, HiddenInput


class Artist(models.Model):
    """
    Artist Model that specifically handles the Artist submissions
    Artist and Echonest ID
    """
    artist = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    """
    Song Model that has a relationship with Artist.
    Song title
    Song's Echonest ID
    """
    song = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    #TODO add request count.

class Submitter(models.Model):
    """
    Record of who submitted a song.
    First & Last Name.
    Email
    Songs_added
    Created date
    Modified date
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    songs_added = models.ManyToManyField(Song)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class SubmitterForm(ModelForm):
    """
    Form class for automatically handled by Django.
    """
    class Meta:
        model = Submitter
        exclude = ('created', 'modified', 'songs_added',)


class ArtistForm(ModelForm):
    """
    Form Class Automatically handled by Django.
    """

    class Meta:
        model = Artist
        widgets = {
            'artist_id': HiddenInput,
        }