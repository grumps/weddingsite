from django_nopassword.forms import AuthenticationForm
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django_nopassword.utils import USERNAME_FIELD
from django_nopassword.models import LoginCode
from django.utils.translation import ugettext_lazy as _
from django_nopassword.views import login_with_code
from braces.views import LoginRequiredMixin
from .models import PrimaryGuest, PrimaryGuestForm, PartnerGuest, PartnerGuestForm
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


class PrimaryGuestRsvp(LoginRequiredMixin, UpdateView):
    template_name = 'rsvp-step2.html'
    login_url = '/rsvp/'
    form_class = PrimaryGuestForm

    def get_object(self, queryset=None):
        #TODO Add Get or 404
        primary = PrimaryGuestForm.Meta.model.objects.get(user=self.request.user)
        if primary.is_allowed_partner:
            self.success_url = '/rsvp/rsvp-step2/rsvp-for-partner/'
        else:
            self.success_url = '/rsvp/rsvp-complete/'
        return primary

class PartnerGuestRsvp(LoginRequiredMixin, UpdateView):
    template_name = 'rsvp-step2.html'
    login_url = '/rsvp/'
    form_class = PartnerGuestForm
    success_url = '/rsvp/rsvp-complete/'

    def get_object(self, queryset=None):
        #TODO Add Get or 404
        primary = PrimaryGuest.objects.get(user=self.request.user.id).pk
        partner = PartnerGuestForm.Meta.model.objects.get(primaryguest_id=primary)
        return partner




