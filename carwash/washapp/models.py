from django.db import models

# Create your models here.

class Client(models.Model):
    name=models.TextField()
    number=models.IntegerField()

class Zayavki(models.Model):
    clientsid = models.ForeignKey(Client, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TextField()

class Timetable(models.Model):
    time=models.TextField()

