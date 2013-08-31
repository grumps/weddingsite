from django.shortcuts import render
from django.forms.models import inlineformset_factory
from wedme.playlistform.models import SubmitterForm, ArtistForm, Artist, Song


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
            if not artist_exists:
                artist.save()
            artist_instance = Artist.objects.get(artist_id=cleaned_artist).pk
            for form in formset:
                song_title = str((form.cleaned_data['song']))
                Song.objects.get_or_create(song=song_title, artist_id=artist_instance)
            submitter.save()

        else:
            return render(request, '/the-wedding-party')
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