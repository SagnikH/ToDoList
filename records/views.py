from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views.generic import DeleteView, ListView, CreateView

from django import forms

from .models import RecordList

from .forms import RecordListForm

# Create your views here.

def recordListView(request) :

    items = RecordList.objects.all()

    if request.method == 'POST' :
        val = request.POST['item']

        if len(val) == 0 :
            error = 'Not a valid Input'
            return render(request, 'index.html', {'items' : items, 'errors' : error})

        RecordList.objects.create(todo=val)

        return redirect('/')

    return render(request, 'index.html', {'items' : items})



# class based ListView
# class RecordListView(ListView) :

#     template_name = "index.html"

#     queryset = RecordList.objects.all()



# def deleteView(request, id) :

#     item = RecordList.objects.get(id=id)

#     if request.method == 'POST' :
#         item.delete()
#         return redirect('/')

#     return render(request, 'delete.html', {'id' : id})



# this is the class based DeleteView
class RecordDeleteView(DeleteView) :

    template_name = "delete.html"
   
    def get_object(self) :
       id_ = self.kwargs.get("pk")
       return get_object_or_404(RecordList, id=id_)

    def get_success_url(self) :
        return reverse("records:todoList")



class RecordCreateView(CreateView) :

    template_name = "create.html"
    form_class = RecordListForm
    success_url = '/'