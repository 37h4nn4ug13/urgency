from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
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
            return redirect("home")
        
        
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, "base/home.html", context)

@login_required # shouldn't need this but it is probably more secure. 
def changeProgress(request):
    if request.method == "GET":
        task_id = request.GET['task_id']
        will_increase = request.GET['will_increase']
        task = Task.objects.get(pk=task_id)
        if will_increase == '1' and task.progress <= 90:
            task.progress += 10
        elif will_increase == '0' and task.progress >= 10:
            task.progress -= 10
        else:
            return HttpResponse("Do Nothing") # this should be for debugging only
        jsonContent = {
            "progress": task.progress
        }
        task.save()
        return JsonResponse(jsonContent)

@login_required
def remove(request):
    if request.method == "GET":
        task_id = request.GET['task_id']
        task = Task.objects.get(pk=task_id)
        task.is_complete = True
        task.save()
        return HttpResponse(task.is_complete)


