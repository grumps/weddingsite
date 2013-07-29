from django.db import models
from django.forms import ModelForm, HiddenInput


class Submitter(models.Model):
    """
    Record of who submitted a song.
    First & Last Name.
    Email
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()


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
    song_id = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist)


class SubmitterForm(ModelForm):
    """
    Form class for automatically handled by Django.
    """
    class Meta:
        model = Submitter


class ArtistForm(ModelForm):
    """
    Form Class Automatically handled by Django.
    """

    class Meta:
        model = Artist
        widgets = {
            'artist_id': HiddenInput,
        }