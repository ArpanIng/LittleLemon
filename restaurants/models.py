from django.db import models
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=200)
    reservation_slot = models.SmallIntegerField(default=10)
    reservation_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name}: {self.reservation_date}"


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_image = models.ImageField(upload_to="menu_items", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
