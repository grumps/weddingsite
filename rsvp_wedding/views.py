from django_nopassword.forms import AuthenticationForm
from django.views.generic.edit import FormView


class RsvpStartView(FormView):
    """
    This class subclasses django_nopassword.forms to start RSVP process.
    """

    template_name = 'rsvp-step1.html'
    form_class = AuthenticationForm
    success_url = 'email-on-the-way'
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #TODO re-direct to "waiting page" with name and partial email info
            return super(RsvpStartView, self).form_valid(form)
        else:
            #TODO get error data back to form.
            return super(RsvpStartView, self).form_invalid(form)