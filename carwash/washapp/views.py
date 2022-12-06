from django.shortcuts import render
from .models import Zayavki, Timetable, Client
from datetime import date, datetime, time, timedelta


""" метод получает все заявки и все шаблонное время из бд
так же получает дату, выбранную пользователем, либо автоматически 
генерирует сегодняшнюю дату. сверяя даты и забронированное время с шаблонами
времени выбираем какое время доступно сохраняем его. возвращаем нужный нам html 
и передаем доступное время, выбранную дату и сегодняшнюю дату """

def getTimeFreeView(request):
    vse_zayav=Zayavki.objects.all()
    vse_time= Timetable.objects.all()
    vse_nuzh=[]
    dely=[]
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
                dely.append(i)
    for j in dely:
        vse_nuzh.remove(j)
    return render(request,'washlist.html', {'req':req,'vse_nuzh':vse_nuzh, 'today':str(date.today())})
    
""" метод считываем имя клиента, номер, выбранное время и дату. далее 
создаем экземпляры класса Клиента и Заявки и заполняем данные, 
почле чего сохраняем данные в бд и возвращаем новый html файл с данными и клиенте и заявке """
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
