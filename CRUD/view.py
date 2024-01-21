from django.shortcuts  import render
from django.http import  HttpResponseRedirect
from django.http import HttpResponse
from home.models import showdata

def show(request):
    data = showdata.objects.all()
    return render(request,"show.html",
   {'Data':data})

def delete(request):
    ID = request.GET['ID']
    showdata.objects.filter(ID = ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID=request.GET['ID']
    Data1 = Data2 = "not Available"
    for data in showdata.objects.filter(ID=ID):
        Data1 = data.Data1
        Data2 = data.Data2
    return render(request,"edit.html",{'ID':ID,'Data1':Data1,'Data2':Data2})


def RecordEdited(request):
    if request.method=='POST':
        ID=request.POST['ID']
        Data1=request.POST['Data1']
        Data2=request.POST['Data2']
        showdata.objects.filter(ID=ID).update(Data1 = Data1,Data2 = Data2)
        return HttpResponseRedirect('show')
    else:
        return HttpResponse("<h1> 404 - Found </h1>")




