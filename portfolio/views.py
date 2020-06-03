from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all() # Get all the objects from the database that are 'project' objects
    
    # pass a template into our dictionary 
    return render(request, 'portfolio/home.html', {'projects': projects})
