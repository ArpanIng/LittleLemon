from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_image = models.ImageField(upload_to="menu_items", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
