from django.shortcuts import render
from .models import Task

# Create your views here.


def index(request):
    if (request.method=="POST"):
        progress = request.POST.get("progress")
        taskid = request.POST.get("taskId")
        task = Task.objects.get(id=taskid)
        task.progress = progress
        task.save()
    context = {
        'tasks': Task.objects.all() 
    }
    return render(request, "base/home.html", context)
