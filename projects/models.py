from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    url = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title