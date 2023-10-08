from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def projects(request):
    project_template = loader.get_template('projects.html')
    return HttpResponse(project_template.render())