from django.contrib import admin
from .models import Appointment, BookingTime, BookingDays, BookingSlots

admin.site.register(Appointment)
admin.site.register(BookingTime)
admin.site.register(BookingDays)
admin.site.register(BookingSlots)

# Register your models here.
