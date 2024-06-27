from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Room(models.Model):
    capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    room_number = models.PositiveIntegerField()
    # reserved_count = models.PositiveIntegerField(default=0)
    remaining_capacity = models.PositiveIntegerField(default=capacity)

    # @property
    # def is_available(self):
    #     return self.capacity - self.reserved_count != 0

    @property
    def is_available(self):
        return self.remaining_capacity - 1 >= 0


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation')
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='reservation')
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(default=timezone.now() + timezone.timedelta(days=30))

    def save(self, *args, **kwargs):
        if self.room.is_available:
            # self.room.reserved_count += 1
            self.room.remaining_capacity -= 1
            self.room.save()
            super().save()

    def room_availability(self):
        ...

