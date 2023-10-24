from django.shortcuts import render
from wand.image import Image
from django.http import HttpResponse, FileResponse, Http404

# Import project models
from home.models import Project, Lab, Game

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

# DEBUG: render the default template
def template(request):
    return render(request, 'pages/template.html')
    path('experience/', views.experience, name='experience'),
# === Navbar ===
def experience(request):
    return render(request, 'pages/experience.html')

def projects(request):
    labs = Lab.objects.all()
    
    # Create a set of preview images for each lab
    for lab in labs:
        with Image(filename=f'static/pdf/labs/{lab.pdf_title}.pdf[0]') as img:
            
            # Create this image under the static folder
            preview_filepath = f'static/pdf/labs/{lab.pdf_title}_preview.png'
            
            img.format = 'png'
            img_width = img.size[0]
            img_height = img.size[1]
            img.crop(width=img_width, height=img_height // 2, gravity='north')
            img.background_color = 'white'
            img.save(filename=preview_filepath)
            
            # Pass the path to the lab object. Make sure the path is relative to the static folder
            lab.static_preview_path = preview_filepath.replace('static/', '')
            
    games = Game.objects.all()
    
    
    return render(
        request,
        'pages/projects.html',
        {
            'labs': labs,
            'games': games
        }
    )


# === Lab Project PDFs ===
def projects_lab(request, pdf_name):
    try:
        lab_path = f'static/pdf/labs/{pdf_name}.pdf'
        return FileResponse(open(lab_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()