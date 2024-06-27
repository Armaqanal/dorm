from room import views
from django.urls import path

app_name = 'room'
urlpatterns = [

    path('available_rooms/', views.available_rooms_view, name='available_rooms'),
    path('reservation/<int:room_id>/', views.reservation, name='reservation')
]
