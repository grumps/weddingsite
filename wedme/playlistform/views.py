from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from wedme.playlistform.models import SubmitterForm, ArtistForm, SongForm, Artist, Song


def playlistAdd(request):
    SongFormInlineSet = inlineformset_factory(Artist, Song, can_delete=False, extra=1, max_num=5)
    SubmitterFormSet = SubmitterForm
    ArtistFormSet = ArtistForm
    if request.method == 'POST':
        formset = SongFormInlineSet(request.POST)
        form2 = ArtistFormSet(request.POST)
        form3 = SubmitterFormSet(request.POST)
        if form.is_valid():
            form.save()
    else:
        formset = SongFormInlineSet()
        form2 = ArtistFormSet()
        form3 = SubmitterFormSet()
    return render(request, 'add-a-jam.html', {
            "formset": formset,
            "form2": form2,
            "form3": form3,
        })


