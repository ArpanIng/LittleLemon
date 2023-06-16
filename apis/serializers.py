from rest_framework import serializers

from restaurants.models import Booking, Menu


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("name", "reservation_slot", "reservation_date")


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "name", "price", "menu_image", "description")
