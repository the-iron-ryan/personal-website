from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template/', views.template, name='template'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('projects/lab/<str:pdf_name>', views.projects_lab, name='projects_lab'),
]
