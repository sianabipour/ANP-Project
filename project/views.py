from django.shortcuts import render
from project.models import Project

def projects(request):
    projects = Project.objects.all().order_by("order_number")
    context= {
        'projects':projects,
    }
    return render(request,'projects.html',context)
def single_project(request,slug):
    project = Project.objects.get(slug=slug)
    context = {
        'projects':project
    }
    return render(request,'single-project.html',context)