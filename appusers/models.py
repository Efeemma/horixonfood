from django.db import models


# Create your models here.

class Menu(models.Model):
    item_photo = models.ImageField(upload_to='products', blank=True)
    name = models.CharField(max_length=20,)
    desc = models.CharField(max_length=50,)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Gallery(models.Model):
    item_photo = models.ImageField(upload_to='gallery', blank=True)



class Reserve(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Adjust max_length as needed
    num_persons = models.IntegerField()
    reservation_datetime = models.DateTimeField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Adjust max_length as needed
    message = models.TextField(max_length=300)