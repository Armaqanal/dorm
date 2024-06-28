from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateRoomForm

from room.models import Room, Reservation


def available_rooms_view(request):
    available_rooms = [room for room in Room.objects.all() if room.is_available]
    # available_rooms = Room.objects.
    print("*" * 50, available_rooms)

    contex = {
        'available_rooms': available_rooms
    }
    return render(request, 'available_rooms.html', contex)


def reservation(request, room_id):
    room = Room.objects.get(id=room_id)
    Reservation.objects.create(room=room, customer=request.user)
    return redirect('account:home')  # TODO


@login_required
def add_rooms(request):
    if request.user.is_superuser:
        form = CreateRoomForm()

        if request.method == 'POST':
            form = CreateRoomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('account:home')
        context = {
            'form': form
        }
        return render(request, 'room_creation_form.html', context)

    else:
        return HttpResponse('Your are not the Manager')
