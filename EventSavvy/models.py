from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)  
    address = models.CharField(max_length=255)  
    city = models.CharField(max_length=255)  
    password= models.CharField(max_length=10)
    
class Organiser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15) 
    experience = models.CharField(max_length=2)  
    city = models.CharField(max_length=255)  
    password = models.CharField(max_length=10)
    
class EventRecord(models.Model):
    event = models.CharField(max_length=255)
    budget = models.CharField(max_length=255)
    no_of_people = models.CharField(max_length=255)
    date = models.DateTimeField()
    content = models.TextField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    organiser_id = models.ForeignKey(Organiser, on_delete=models.CASCADE , default=1)

class OrganiserRecord(models.Model):
    organiser = models.ForeignKey(Organiser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    tagline = models.CharField(max_length=255)

class Expense(models.Model):
    organiser = models.ForeignKey(Organiser, on_delete=models.CASCADE, default=1)
    event = models.ForeignKey(EventRecord, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()