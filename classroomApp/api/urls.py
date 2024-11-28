from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("rooms/", views.getRooms),
    path("rooms/<str:pk>/", views.getRoom),
]