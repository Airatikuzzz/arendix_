from django import forms

class RoomsFilterForm(forms.Form):
    min_square = forms.IntegerField(label="from", required=False)
    max_square = forms.IntegerField(label="to", required=False)
    min_price_per_m2 = forms.IntegerField(label="from", required=False)
    max_price_per_m2 = forms.IntegerField(label="to", required=False)
    min_price = forms.IntegerField(label="from", required=False)
    max_price = forms.IntegerField(label="to", required=False)
