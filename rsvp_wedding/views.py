from django_nopassword.forms import AuthenticationForm
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render
from django_nopassword.utils import USERNAME_FIELD
from django_nopassword.models import LoginCode
from django.utils.translation import ugettext_lazy as _
from django_nopassword.views import login_with_code
from braces.views import LoginRequiredMixin
from .models import PrimaryGuest
from django.contrib.auth.models import User


class RsvpStartView(FormView):
    """
    Subclasses django_nopassword.forms to start RSVP process.
    """
    template_name = 'rsvp-step1.html'
    form_class = AuthenticationForm
    # Override Error Messages from default form
    AuthenticationForm.error_messages = {
        'invalid_login': _("Please enter the email address we told you to use. "
                           "Note that the field is case-sensitive and you should use all lower case letters. Contact us if you're having issues."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("This account is inactive."),
    }

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            code = LoginCode.objects.filter(**{'user__%s' % USERNAME_FIELD: request.POST.get('username')})[0]
            code.next = '/rsvp/step2/'
            code.save()
            code.send_login_email()
            email = form.cleaned_data['username']
            return render(request, 'email-on-the-way.html', {
                'guest_email': email,
            })
        else:
            return super(RsvpStartView, self).form_invalid(form)


class RsvpStepTwoView(LoginRequiredMixin, UpdateView):
    uid = request.user
    print uid
    model = PrimaryGuest
