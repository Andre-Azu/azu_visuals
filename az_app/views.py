from django.shortcuts import render
from .models import Image
# Create your views here.
def all_images(request):
    images=Image.objects.all()
    return render(request, 'az_app/home.html', {'images':images})
