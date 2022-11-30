from django.contrib import admin

from .models import Zayavki, Client, Timetable

admin.site.register(Zayavki)
admin.site.register(Client)
admin.site.register(Timetable)

# Register your models here.
