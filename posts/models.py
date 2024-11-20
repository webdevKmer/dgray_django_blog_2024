from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=80)
  body = models.TextField()
  slug = models.SlugField()
  created_at = models.DateTimeField(auto_now_add=True)