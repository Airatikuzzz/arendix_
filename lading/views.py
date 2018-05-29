from django.shortcuts import render, get_object_or_404, redirect
from rooms.models import RoomImage, Room, Status
from rooms.forms import RoomsFilterForm, RoomImageForm
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
    return render(request, 'room_detail1.html', {'room_image': room, "username": auth.get_user(request).username})
def scheme(request):
    rooms = RoomImage.objects.all;
    return render(request, 'scheme.html', {"rooms": rooms, "username": auth.get_user(request).username})
def about(request):
    return render(request, 'about.html', {"username": auth.get_user(request).username})
def add_room(request):
    print(request.POST)
    form = RoomImageForm()
    print(request.method)

    if request.method == "POST":
        form = RoomImageForm(request.POST)
        #print(form)
        room = Room()
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.square = request.POST.get('square')
        room.price_per_m2 = request.POST.get('price_per_m2')
        room.price = request.POST.get('price')
        room.comments = request.POST.get('comments')
        room.status = get_object_or_404(Status, pk=2)
        room.save()
        roomImage = RoomImage()
        roomImage.room = get_object_or_404(Room, pk=room.pk)
        roomImage.image = request.POST.get('image')
        roomImage.save()
        return redirect('/')
    return render(request, 'add_room.html', {"form":form,"username": auth.get_user(request).username})
