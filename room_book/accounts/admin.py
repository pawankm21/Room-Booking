from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number']


class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'booking_time_from', 'booking_time_to')


admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
