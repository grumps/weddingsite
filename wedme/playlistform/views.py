from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import modelformset_factory
from wedme.playlistform.models import SubmitterForm, ArtistForm, SongForm


def playlistAdd(request):
    return HttpResponse("hello, world")
    # SubmitterFormSet = modelformset_factory(SubmitterForm)
    # if request.method == 'POST':
    #     formset = SubmitterFormSet(request.POST)
    #     if formset.is_valid():
    #         formset.save()
    #     else:
    #         formset = SubmitterFormSet()
    #     return render_to_response('add-a-jam.html', {
    #         "formset": formset,
    #     })