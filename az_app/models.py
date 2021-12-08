from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

    
class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')

    
class Location(models.Model):
    location_area=models.CharField(max_length=30)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    
    def __str__(self):
        return self.location_area
    
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()


class Category(models.Model):
    category_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name

class Image(models.Model):
    image=models.ImageField(upload_to='pics_gallery/', default=None)
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()    
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default=None)      
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default=None)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(image__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images

    @classmethod
    def view_by_category(cls, category):
        images=cls.objects.filter

class Meta:
    ordering = ['-post_time']