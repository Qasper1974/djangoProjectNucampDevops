from django.shortcuts import render

from .models import Room

# Create your views here.

# rooms =[
# { 'id': 1, 'name' : 'Lets learn Python'},
# { 'id': 2, 'name' : 'Design with me'},
# { 'id': 3, 'name' : 'Frontend Developers'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'kamers': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    kamer = Room.objects.get(id=pk)
    context = {'room': kamer}
    return render(request, 'base/room.html', context)
