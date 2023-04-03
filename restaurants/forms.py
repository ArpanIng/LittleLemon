from django import forms

from .models import Booking


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("first_name", "last_name", "no_of_guests", "comments")
