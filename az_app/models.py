from django.db import models

# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='pics_gallery/', default=None)
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()
    