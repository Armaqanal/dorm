from django import forms

from room import models


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'
        # exclude = ['remaining_capacity']
