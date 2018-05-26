from django.shortcuts import render, get_object_or_404
from rooms.models import RoomImage
from rooms.forms import RoomsFilterForm
from django.contrib import auth

# Create your views here.
def home(request):
    rooms = RoomImage.objects.all();
    form = RoomsFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_square"]:
            rooms = rooms.filter(room__square__gte=form.cleaned_data["min_square"])
        if form.cleaned_data["max_square"]:
            rooms = rooms.filter(room__square__lte=form.cleaned_data["max_square"])
        if form.cleaned_data["min_price_per_m2"]:
            rooms = rooms.filter(room__price_per_m2__gte=form.cleaned_data["min_price_per_m2"])
        if form.cleaned_data["max_price_per_m2"]:
            rooms = rooms.filter(room__price_per_m2__lte=form.cleaned_data["max_price_per_m2"])
        if form.cleaned_data["min_price"]:
            rooms = rooms.filter(room__price__gte=form.cleaned_data["max_price"])
        if form.cleaned_data["max_price"]:
            rooms = rooms.filter(room__price__lte=form.cleaned_data["max_price"])
    context = {"rooms": rooms, "form": form, "username": auth.get_user(request).username}
    return render(request, 'home.html', context)
def room_detail(request, pk):
    room = get_object_or_404(RoomImage, pk=pk)
    return render(request, 'room_detail.html', {'room_image': room, "username": auth.get_user(request).username})
def scheme(request):
    rooms = RoomImage.objects.all;
    return render(request, 'scheme.html', {"rooms": rooms, "username": auth.get_user(request).username})
def about(request):
    return render(request, 'about.html', {"username": auth.get_user(request).username})
def add_room(request):
    return render(request, 'add_room.html', {"username": auth.get_user(request).username})
