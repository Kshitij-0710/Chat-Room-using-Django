from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')

    if Room.objects.filter(name=room).exists():
        return redirect(reverse('room', args=[room]) + f'?username={username}')
    else:
        new_room = Room.objects.create(name=room)
        return redirect(reverse('room', args=[room]) + f'?username={username}')

def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = get_object_or_404(Room, name=room)
    messages = Message.objects.filter(room=room_details.id).values()
    return JsonResponse({"messages": list(messages)})
