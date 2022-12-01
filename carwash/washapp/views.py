from django.shortcuts import render
from .models import Zayavki, Timetable

def washappView(request):
    vse_zayav=Zayavki.objects.all()
    vse_time= Timetable.objects.all()
    #req=request.POST['datewash']
    #for i in vse_zayav:
        #if i.date==req:
            #vse_time.filter(id=i.id).delete()
    return render(request,'washlist.html', {'all_zayav':vse_zayav,'all_time':vse_time})

def getTimeFreeView(request):
    vse_zayav=Zayavki.objects.all()
    vse_time= Timetable.objects.all()
    req=request.POST['datewash']
    for i in vse_zayav:
        if i.date==req:
            vse_time.filter(id=i.id).delete()
    return render(request,'timefree.html', {'all_zayav':vse_zayav,'all_time':vse_time})
    return HttpResponseRedirect('/todoapp')
    return render(request,'todolist.html',{'i':new_item})

