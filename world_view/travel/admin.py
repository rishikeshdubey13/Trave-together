from django.contrib import admin
from .models import Destination, Accomodation, Transport, Customer, Bookings

# Register your models here.
admin.site.register(Destination)
admin.site.register(Accomodation)
admin.site.register(Transport)
admin.site.register(Customer)
admin.site.register(Bookings)