from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

# DEBUG: render the default template
def template(request):
    return render(request, 'pages/template.html')