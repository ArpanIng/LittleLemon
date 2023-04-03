from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("menu/<int:pk>/", views.menu_item, name="menu_item"),
    path("booking/", views.booking, name="booking"),
]
