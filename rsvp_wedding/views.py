from django_nopassword.forms import AuthenticationForm
from django.views.generic.edit import FormView

from django_nopassword.utils import USERNAME_FIELD, get_username
from django_nopassword.models import LoginCode


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
            code = LoginCode.objects.filter(**{'user__%s' % USERNAME_FIELD: request.POST.get('username')})[0]
            code.next = request.GET.get('next')
            code.save()
            code.send_login_email()
            return super(RsvpStartView, self).form_valid(form)
        else:
            #TODO get error data back to form.
            return super(RsvpStartView, self).form_invalid(form)