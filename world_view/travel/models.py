from django.db import models

# Create your models here.
class  Destination(models.Model):
    name = models.CharField(max_length = 100)
    descripton = models.CharField(max_length=500)
    country = models.TextField(max_length=100)

    def __str__ (self):
        return self.name


class Accomodation(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    description = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)

    def __str__ (self):
        return self.name


class Transport(models.Model):
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    origin = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)


class Customer(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.EmailField(max_length=50)
    phone  = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Bookings(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)

    def __str__ (self):
        return f'{self.customer} {self.destination}'


# class Activity(models.Model):
