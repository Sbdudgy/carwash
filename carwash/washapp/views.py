from django.shortcuts import render
from .models import Zayavki, Timetable, Client
from datetime import date, datetime, time, timedelta

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
    if req==str(date.today()):
        a = datetime.now().time()   
        for i in vse_nuzh:
            b=time(int(i.split(':')[0]),int(i.split(':')[1]),0)
            d1 = timedelta(hours=a.hour, minutes=a.minute, seconds=a.second)
            d2 = timedelta(hours=b.hour, minutes=b.minute, seconds=b.second)
            if d1>d2:
                vse_nuzh.remove(i)
    return render(request,'washlist.html', {'all_zayav':vse_zayav,'all_time':vse_time,'req':req,'vse_nuzh':vse_nuzh, 'today':str(date.today())})
    

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
