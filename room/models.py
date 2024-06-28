from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class RoomManager(models.Manager):
    def get_available_rooms(self):
        return self.filter(is_available=True)


class Room(models.Model):
    def default_remaining_capacity(self):
        return self.capacity

    capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    room_number = models.PositiveIntegerField()

    # ____________________________(way 2) ___________________________________________
    # is_available = models.BooleanField(default=True)
    # objects = RoomManager()
    # ____________________________(way 2) ___________________________________________

    # ____________________________(way 1) ___________________________________________
    @property
    def remaining_capacity(self):
        return self.capacity - self.reservation.filter(end_date__gt=timezone.now()).count()

    @property
    def is_available(self):
        return self.remaining_capacity > 0

    # ____________________________(way 1) ___________________________________________

    # ____________________________(way 2) ___________________________________________

    # @property
    # def is_available(self):
    #     return self.remaining_capacity - 1 >= 0
    #
    # def save(self):
    #     self.remaining_capacity = self.capacity
    #     super(Room, self).save()

    # @property
    # def is_available(self):
    #     return self.capacity - self.reserved_count != 0

    def save(self, *args, **kwargs):
        self.is_available = self.remaining_capacity > 0
        super(Room, self).save(*args, **kwargs)

    # TODO: free room capacity


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation')
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='reservation')
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(default=timezone.now() + timezone.timedelta(days=30))

    # def save(self, *args, **kwargs):
    #     self.room.save()
    #
    #     if self.room.is_available:
    # self.room.reserved_count += 1
    # self.room.remaining_capacity -= 1
    # self.room.save()
    # super(Reservation, self).save()
    # else:
    #     raise ValueError('Room is not available')

    def room_availability(self):
        ...
