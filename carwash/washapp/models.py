from django.db import models

# Create your models here.

class Zayavki(models.Model):
    content=models.TextField()
    clientsid = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TextField()



