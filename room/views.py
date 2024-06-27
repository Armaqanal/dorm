from django.shortcuts import render, redirect

from room.models import Room, Reservation


# Create your views here.


def available_rooms_view(request):
    # show_available_room = Room.objects.all()
    available_rooms = Room.objects.filter(remaining_capacity__gt=0)
    contex = {
        'available_rooms': available_rooms
    }
    return render(request, 'available_rooms.html', contex)


def reservation(request, room_id):
    room = Room.objects.get(id=room_id)
    Reservation.objects.create(room=room, customer=request.user)
    return redirect('account:home')  # TODO

# def add_rooms(request):
#     if request.user.is_superuser:
#         if request.method=='POST':
#             form=
#         room=Room.objects.create(capacity=capacity,
