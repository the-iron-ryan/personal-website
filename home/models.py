from typing import Any
from django.db import models

# Create your models here.

# ==================== #
# Base Project Model
# ==================== #
class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    
    class Meta:
        # Make this an abstract class so that it wont be created in the database
        abstract = True

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.static_preview_path = ''
    

class Lab(Project):
    pdf_title = models.CharField(max_length=100)
    abstract = models.TextField(default="")
    
    class Meta:
        db_table = 'home_lab'
    
class Game(Project):
    url = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'home_game'
    

