from django.db import models

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.slot_number


class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
