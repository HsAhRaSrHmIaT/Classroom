from django.forms import ModelForm #type: ignore
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants', 'date_created', 'date_updated']