from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingModelForm
from .models import Menu


def homepage(request):
    return render(request, "restaurants/index.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    menus = Menu.objects.all()

    context = {
        "menus": menus,
    }
    return render(request, "restaurants/menu.html", context)


def menu_item(request, pk):
    menu = get_object_or_404(Menu, id=pk)

    context = {
        "menu": menu,
    }
    return render(request, "restaurants/menu_item.html", context)


def booking(request):
    form = BookingModelForm()
    if request.method == "POST":
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu")

    context = {
        "form": form,
    }
    return render(request, "restaurants/booking.html", context)
