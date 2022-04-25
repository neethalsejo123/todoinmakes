from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Taskt
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class Taskupdateview(UpdateView):
    model = Taskt
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Taskt
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

class Tasklistview(ListView):
    model = Taskt
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Taskt
    template_name = 'detail.html'
    context_object_name = 'task'


# Create your views here.

def home(request):
    task1 = Taskt.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Taskt(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    task = Taskt.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Taskt.objects.get(id=id)
    f = Todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})