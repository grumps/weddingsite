from django.db import models
from django.contrib import auth
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, MultiField


class WeddingGuestModel(models.Model):
    """
    An abstract base class model that provides basic data for guests.
    """
    ATTENDANCE = (
        ('Y', "Will Be there"),
        ('N', "Won't Be there."),
    )

    VEGGIE = (
        ('Y', 'Vegetarian'),
        ('N', 'Omnivore'),
    )
    will_arrive_thursday = models.CharField(max_length=1, choices=ATTENDANCE,)
    will_stay_saturday = models.CharField(max_length=1, choices=ATTENDANCE)
    will_attend = models.CharField(max_length=1, choices=ATTENDANCE)
    is_vegetarian = models.CharField(max_length=1, choices=VEGGIE)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PrimaryGuest(WeddingGuestModel, TimeStampedModel):
    user = models.OneToOneField("auth.User")
    is_allowed_partner = models.BooleanField()


class PartnerGuest(WeddingGuestModel, TimeStampedModel):
    first_name = models.CharField(max_length=140, default="NULL")
    last_name = models.CharField(max_length=140, default="NULL")
    primaryguest = models.ForeignKey(PrimaryGuest)


class PrimaryGuestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrimaryGuestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = PrimaryGuest
        fields = ['will_attend', 'will_arrive_thursday', 'will_stay_saturday', 'is_vegetarian']


class PartnerGuestForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PartnerGuestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout (
            Div(
                'has-switch',
                'switch-animate',
                'switch-off',
            ),
        )


    class Meta:
        model = PartnerGuest
        fields = ['will_attend', 'will_arrive_thursday', 'will_stay_saturday', 'is_vegetarian']