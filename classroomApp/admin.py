from django.contrib import admin #type: ignore
from .models import Room, Topic, Message #type: ignore


# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
