from django.shortcuts import render,redirect
from django.urls import reverse

from .models import RecordList

# Create your views here.

def recordListView(request) :

    items = RecordList.objects.all()

    return render(request, 'index.html', {'items' : items})

def deleteView(request, id) :

    item = RecordList.objects.get(id=id)

    if request.method == 'POST' :
        item.delete()
        return redirect('/')

    return render(request, 'delete.html', {'id' : id})

