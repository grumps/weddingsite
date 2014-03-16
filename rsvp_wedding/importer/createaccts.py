from django.contrib.auth.models import User
from rsvp_wedding.models import PrimaryGuest, PartnerGuest
import csv


with open('GuestList-Test.csv','rb') as guestlist:
    guests = csv.reader(guestlist)
    for guest in guests:
        if guest[5] == 'y':
            UserInstace = User.objects.create(username=guest[4], first_name=guest[0], last_name=guest[1], email=guest[4])
            primary_guest_added = PrimaryGuest.objects.create(user=UserInstace, is_allowed_partner=1)
            partner_guest = PartnerGuest.objects.create(primaryguest=primary_guest_added, first_name=guest[2], last_name=guest[3])
            print primary_guest_added.user.first_name, primary_guest_added.user.last_name, primary_guest_added.user
            print partner_guest.first_name, partner_guest.last_name
            print '#######################################'

        else:
            UserInstace = User.objects.create(username=guest[4], first_name=guest[0], last_name=guest[1], email=guest[4])
            primary_guest = PrimaryGuest.objects.create(user=UserInstace, is_allowed_partner=0)
            print primary_guest_added.user.first_name, primary_guest_added.user.last_name, primary_guest_added.user
            print '#######################################'

