from django.db import models


class Booking(models.Model):

    ROOM_CHOICES = (
        ('Deluxe Room', 2500),
        ('Premium Room', 4500),
        ('Suite Room', 7000),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    room = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    total_bill = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name