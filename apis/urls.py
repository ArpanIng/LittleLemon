from django.urls import path

from . import views

app_name = "apis"
urlpatterns = [
    path("bookings/", views.BookingView.as_view(), name="bookings"),
    path(
        "bookings/<int:pk>/",
        views.BookingDetailView.as_view(),
        name="booking_detail",
    ),
    path("menu-items/", views.MenuView.as_view(), name="menu"),
    path("menu-items/<int:pk>/", views.MenuDetailView.as_view(), name="menu_detail"),
]
