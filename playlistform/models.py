from django.db import models
from django.forms import ModelForm, HiddenInput


class TimeStampedModel(models.Model):
    """
    Class for managing timestamps and update stamps.
    Thanks to 2 Scoops of Django for this.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artist(TimeStampedModel):
    """
    Artist Model that specifically handles the Artist submissions
    Artist and Echonest ID
    """
    artist = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Song(TimeStampedModel):
    """
    Song Model that has a relationship with Artist.
    Song title
    Song's Echonest ID
    """
    #TODO rename this field. Will break: /wedme/playlistform/templates/thank-you.html:18 {{ song.song }}
    song = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    request_count = models.IntegerField(default=1)


class Submitter(TimeStampedModel):
    """
    Record of who submitted a song.
    First & Last Name.
    Email
    Songs_added
    Created date
    Modified date
    """
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    songs_added = models.ManyToManyField(Song)


class SubmitterForm(ModelForm):
    """
    Form class for automatically handled by Django.
    """
    class Meta:
        model = Submitter
        fields = {
            'first_name',
            'last_name',
            'email',
        }


class ArtistForm(ModelForm):
    """
    Form class automatically handled by Django.
    """

    class Meta:
        model = Artist
        widgets = {
            'artist_id': HiddenInput,
        }