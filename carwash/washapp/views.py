from django.shortcuts import render
from .models import Zayavki, Timetable
from datetime import date

def washappView(request):
    vse_zayav=Zayavki.objects.all()
    vse_time= Timetable.objects.all()
    return render(request,'washlist.html', {'all_zayav':vse_zayav,'all_time':vse_time})

def getTimeFreeView(request):
    vse_zayav=Zayavki.objects.all()
    vse_time= Timetable.objects.all()
    vse_nuzh=[]
    for k in vse_time:
        vse_nuzh.append(k.time)
    if request.POST:
        req=request.POST['datewash']
    else:
        req=str(date.today())
    for i in vse_zayav:
        if str(i.date)==str(req):
            #vse_time.filter(time=i.time).delete()
            vse_nuzh.remove(i.time)
        #else:
            #vse_time= Timetable.objects.all()


    return render(request,'washlist.html', {'all_zayav':vse_zayav,'all_time':vse_time,'req':req,'vse_nuzh':vse_nuzh})
    

