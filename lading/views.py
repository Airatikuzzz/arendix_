from django.shortcuts import render, get_object_or_404
from rooms.models import RoomImage
from rooms.forms import RoomsFilterForm

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
    context = {"rooms": rooms, "form": form}
    return render(request, 'home.html', context)
def room_detail(request, pk):
    room = get_object_or_404(RoomImage, pk=pk)
    return render(request, 'room_detail.html', {'room_image': room})
def scheme(request):
    rooms = RoomImage.objects.all;
    return render(request, 'scheme.html', locals())
def about(request):
    rooms = RoomImage.objects.all;
    return render(request, 'about.html', locals())
