from django.shortcuts import render
from django.forms.models import inlineformset_factory
from wedme.playlistform.models import SubmitterForm, ArtistForm, Artist, Song, Submitter as Submitter_model


def playListAdd(request):
    """
    Handles all playlist add requests.
    """

    SongFormInlineSet = inlineformset_factory(Artist, Song, can_delete=False,
                                              extra=1, max_num=5, exclude=('artist_id', 'request_count'))
    SubmitterFormSet = SubmitterForm
    ArtistFormSet = ArtistForm

    if request.method == 'POST':
        formset = SongFormInlineSet(request.POST)
        artist = ArtistFormSet(request.POST)
        submitter = SubmitterFormSet(request.POST)
        if artist.is_valid() and formset.is_valid() and submitter.is_valid():
            #get cleaned data & cast as string.
            cleaned_artist_name = str((artist.cleaned_data['artist']))
            cleaned_artist_id = str((artist.cleaned_data['artist_id']))
            artist_exists = Artist.objects.filter(artist_id=cleaned_artist_id).exists()

            #add artist to db if artist isn't present.
            if not artist_exists:
                artist.save()
            artist_instance = Artist.objects.get(artist_id=cleaned_artist_id).pk

            #use email for primary look up - for lack of better key. names can alter.
            submitted_email = str(submitter.cleaned_data['email'])
            submitted_exists = Submitter_model.objects.filter(email=submitted_email).exists()
            if not submitted_exists:
                submitter_object = submitter.save()
            else:
                submitter_object = Submitter_model.objects.get(email=submitted_email)
                submitter_object.save()

            for form in formset:
                song_title = str((form.cleaned_data['song']))
                #get_or_create returns tuple of 'obj, [True if created]'
                song_object, song_exists = Song.objects.get_or_create(song=song_title, artist_id=artist_instance)
                submitter_object.songs_added.add(song_object)
                if not (song_exists or Submitter_model.objects.filter(songs_added=song_object.pk).exists()):
                    song_object.request_count += 1
                    song_object.save()
            #Submitter

            #Query Sets for thank-you page
            songs_requested = Song.objects.filter(artist=artist_instance).order_by('-modified', 'song')[:15]
        #redirect back to form.
        else:
            return render(request, 'add-a-jam.html', {
                          "formset": formset,
                          "artist": artist,
                          "submitter": submitter,
                          })
            #form processing complete
        return render(request, 'thank-you.html', {
                      "songs_requested": songs_requested,
                      "submitter": submitter_object,
                      "artist": cleaned_artist_name,
                      })
    else:
        formset = SongFormInlineSet()
        artist = ArtistFormSet()
        submitter = SubmitterFormSet()

    return render(request, 'add-a-jam.html', {
                 "formset": formset,
                 "artist": artist,
                 "submitter": submitter,
                  })