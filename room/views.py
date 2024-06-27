from django.shortcuts import render

from room.models import Room


# Create your views here.


def available_rooms_view(request):
    # show_available_room = Room.objects.all()
    available_rooms = Room.objects.filter(remaining_capacity__gt=0)
    contex = {
        'available_rooms': available_rooms
    }
    return render(request, 'home.html', contex)