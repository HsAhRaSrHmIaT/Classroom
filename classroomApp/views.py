from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponse # type: ignore

# rooms = [
#     {'id': 1, 'name': 'Room 1'},
#     {'id': 2, 'name': 'Room 2'},
#     {'id': 3, 'name': 'Room 3'},
# ]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            return redirect("register")
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")

    context = {'page': page}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

def registerPage(request):
    page = 'register'
    if request.user.is_authenticated:
            return redirect("home")
    
    if request.method == "POST":    
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Account already exists, try logging in")
            return redirect("login")
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "User created successfully")
                return redirect("login")
            except:
                messages.error(request, "An error occurred while creating user")

    context = {'page': page}
    return render(request, "base/login_register.html", context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
            Q(topic__name__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(host__username__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
    }
    return render(request, "base/home.html", context)

@login_required(login_url='/login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, "base/room.html", context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    return render(request, "base/room_form.html", context={'form': form})

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed to edit this room")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    return render(request, "base/room_form.html", context={'form': form})

@login_required(login_url='/login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed to delete this room")
    
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", context={'room': room})


