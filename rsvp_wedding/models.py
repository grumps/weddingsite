from django.db import models
from django_nopassword.models import LoginCode


class WeddingGuestModel(models.Model):
    """
    An abstract base class model that provides basic data for guests.
    """
    will_arrive_thursday = models.BooleanField()
    will_stay_saturday = models.BooleanField()
    will_attend = models.BooleanField()
    is_vegetarian = models.BooleanField()
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


class SecondPartner(WeddingGuestModel, TimeStampedModel):
    partner = models.OneToOneField(PrimaryGuest, related_name="guest_primary")

