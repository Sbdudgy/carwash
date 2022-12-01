from django.shortcuts import render
from .models import Zayavki, Timetable, Client
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
            vse_nuzh.remove(i.time)
    return render(request,'washlist.html', {'all_zayav':vse_zayav,'all_time':vse_time,'req':req,'vse_nuzh':vse_nuzh})
    

def AddNewZayavView(request):
    reqname=request.POST['client_name']
    reqnumb=request.POST['client_numb']
    sel=request.POST['select']
    req=request.POST['rec']
    cl=Client(name=reqname,number=reqnumb)
    cl.save()
    zayavka=Zayavki(clientsid=cl,date=req,time=sel)
    zayavka.save()
    return render(request,'success.html', {'client':cl, 'zayavka':zayavka})
