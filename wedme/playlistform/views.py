from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from wedme.playlistform.models import SubmitterForm, ArtistForm, Artist, Song


def playListAdd(request):
    SongFormInlineSet = inlineformset_factory(Artist, Song, can_delete=False, extra=1, max_num=5, )
    SubmitterFormSet = SubmitterForm
    ArtistFormSet = ArtistForm
    if request.method == 'POST':
        formset = SongFormInlineSet(request.POST)
        artist = ArtistFormSet(request.POST)
        submitter = SubmitterFormSet(request.POST)
        if form.is_valid():
            form.save()
    else:
        formset = SongFormInlineSet()
        artist = ArtistFormSet()
        submitter = SubmitterFormSet()
    return render(request, 'add-a-jam.html', {
        "formset": formset,
        "artist": artist,
        "submitter": submitter,
    })


