from django.shortcuts import render
from django.forms.models import inlineformset_factory
from wedme.playlistform.models import SubmitterForm, ArtistForm, Artist, Song, Submitter as submitter_model


def playListAdd(request):
    SongFormInlineSet = inlineformset_factory(Artist, Song, can_delete=False,
                                              extra=1, max_num=5, exclude=('artist_id',))
    SubmitterFormSet = SubmitterForm
    ArtistFormSet = ArtistForm
    #TODO Handle POST
    if request.method == 'POST':
        formset = SongFormInlineSet(request.POST)
        artist = ArtistFormSet(request.POST)
        submitter = SubmitterFormSet(request.POST)
        if artist.is_valid() and formset.is_valid() and submitter.is_valid():
            #get cleaned data & cast as string.
            cleaned_artist = str((artist.cleaned_data['artist_id']))
            artist_exists = Artist.objects.filter(artist_id=cleaned_artist).exists()
            #add artist to db if artist isn't present.
            if not artist_exists:
                artist.save()
            artist_instance = Artist.objects.get(artist_id=cleaned_artist).pk

            submitter_object = submitter.save()
            for form in formset:
                song_title = str((form.cleaned_data['song']))
                #get_or_create returns tuple of 'obj, [True if created]'
                song_object, song_exists = Song.objects.get_or_create(song=song_title, artist_id=artist_instance)
                submitter_object.songs_added.add(song_object)


        #invalid page
        else:
            return render(request, '/the-wedding-party/')
        return render(request, 'index.html')
    else:
        formset = SongFormInlineSet()
        artist = ArtistFormSet()
        submitter = SubmitterFormSet()
    return render(request, 'add-a-jam.html', {
        "formset": formset,
        "artist": artist,
        "submitter": submitter,
    })
