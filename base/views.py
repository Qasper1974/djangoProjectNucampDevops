from django.shortcuts import render

# Create your views here.

rooms =[
{ 'id': 1, 'name' : 'Lets learn Python'},
{ 'id': 2, 'name' : 'Design with me'},
{ 'id': 3, 'name' : 'Frontend Developers'},

]


def home(request):
    context = {'kamers': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    kamer = None
    
    for i in rooms:
        if i['id'] == int(pk):
            kamer = i
    context = {'room': kamer}
    return render(request, 'base/room.html', context)
