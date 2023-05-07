from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("menu/", views.MenusView.as_view(), name="menu"),
    path("menu/<int:pk>/", views.MenuItemView.as_view(), name="menu_item"),
    path("reservation/", views.reservations, name="reservations"),
    path("book/", views.book, name="book"),
    path("bookings/", views.bookings, name="bookings"),
]
