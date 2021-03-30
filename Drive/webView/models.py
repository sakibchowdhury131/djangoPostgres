from django.db import models

# Create your models here.

class ImageView(models.Model):
    name = models.ImageField(upload_to = 'pics')
    description = models.TextField(max_length= 200)