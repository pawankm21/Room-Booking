from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

    '''user_name = models.CharField(max_length=250)
    user_password = models.CharField(max_length=250)'''


class Room(models.Model):
    room_number = models.CharField(max_length=50)
    room_type = models.fields.CharField(max_length=50, default='Class')

    def __str__(self):
        return self.room_number


class Booking(models.Model):
    STATUS = (
        ('Booked', 'Booked'),
        ('Available', 'Available'),
    )
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    booking_status = models.CharField(max_length=50, null=True, choices=STATUS)
    booking_time_from = models.TimeField(auto_now_add=False, null=True)
    booking_time_to = models.TimeField(auto_now_add=False, null=True)
    booking_date = models.DateField(auto_now_add=False, null=True)
    booking_info =models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.user.name
