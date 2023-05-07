import json
from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt


from .forms import BookingModelForm
from .models import Menu, Booking


class HomepageView(generic.TemplateView):
    template_name = "restaurants/index.html"


class AboutView(generic.TemplateView):
    template_name = "about.html"


class MenusView(generic.ListView):
    queryset = Menu.objects.all()
    context_object_name = "menus"
    template_name = "restaurants/menu.html"


class MenuItemView(generic.DetailView):
    queryset = Menu.objects.all()
    context_object_name = "menu"
    template_name = "restaurants/menu_item.html"


def book(request):
    form = BookingModelForm()
    if request.method == "POST":
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }
    return render(request, "restaurants/booking.html", context)


def reservations(request):
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize("json", bookings)
    return render(request, "restaurants/bookings.html", {"bookings": booking_json})


@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist == False:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error': 1}", content_type="application/json")

    date = request.GET.get("date", datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize("json", bookings)

    return HttpResponse(booking_json, content_type="application/json")
