from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

@login_required
def index(request):
    if (request.method=="POST"):
        taskTitle = request.POST.get("taskTitle")
        taskDescription = request.POST.get("taskDescription")
        ntask = Task()
        ntask.title = taskTitle
        ntask.description = taskDescription
        ntask.user = request.user
        ntask.color = request.POST.get("color")
        if ntask.title is not None:
            ntask.save()
        progress = request.POST.get("progress")
        taskid = request.POST.get("taskId")
        if taskid is not None:
            task = Task.objects.get(id=taskid)
            task.progress = progress
            task.save()
        
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, "base/home.html", context)
