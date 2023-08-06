from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255) 
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_modification = models.DateTimeField(auto_now=True)