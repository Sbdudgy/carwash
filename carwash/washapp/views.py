from django.shortcuts import render
from .models import Zayavki, Timetable

def washappView(request):
    vse_zayav=Zayavki.objects.all()
    vse_time= Timetable.objects.all()
    return render(request,'washlist.html', {'all_zayav':vse_zayav},{'all_time':vse_time})

