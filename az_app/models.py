from django.db import models

# Create your models here.

    
class Location(models.Model):
    location_area=models.CharField(max_length=30)
    def __str__(self):
        return self.location_area

class Category(models.Model):
    category_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name

class Image(models.Model):
    image=models.ImageField(upload_to='pics_gallery/', default=None)
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default=None)
    category=models.ManyToManyField(Category)  

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()
