from django_nopassword.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django import forms


class RsvpStartView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/email-on-the-way/'

    def get_form(self, form_class):
        form = form_class(**self.get_form_kwargs())
        form.fields['username'] = AuthenticationForm.username()
        return form