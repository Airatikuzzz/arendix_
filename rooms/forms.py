from django import forms
from .models import RoomImage

class RoomsFilterForm(forms.Form):
    min_square = forms.IntegerField(label="from", required=False)
    max_square = forms.IntegerField(label="to", required=False)
    min_price_per_m2 = forms.IntegerField(label="from", required=False)
    max_price_per_m2 = forms.IntegerField(label="to", required=False)
    min_price = forms.IntegerField(label="from", required=False)
    max_price = forms.IntegerField(label="to", required=False)

class RoomImageForm(forms.Form):
    name = forms.CharField(label="Название", required=True, widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    description = forms.CharField(label="Описание", required=True)
    square = forms.IntegerField(label="Площадь", required=True)
    price_per_m2 = forms.IntegerField(label="Цена за м2", required=True)
    price = forms.IntegerField(label="Цена", required=True)
    comments = forms.CharField(label="Комментарии", required=False)
    image = forms.ImageField(label="Фотография", required=True)
