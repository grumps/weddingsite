from django.contrib.auth.models import User
from rsvp_wedding.models import PrimaryGuest, PartnerGuest
import csv

def guest_from_file():
    with open('wedding-guest-list.csv','rb') as guestlist:
        guests = csv.reader(guestlist)
        for mainguest in guests:
            if mainguest[5] == 'y':
                primaryguest = PrimaryGuest.objects.create(user=mainguest[4], first_name=mainguest[0], last_name=mainguest[1], is_all)
