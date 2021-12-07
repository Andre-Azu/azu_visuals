from django.shortcuts import render
from .models import Image

def all_images(request):
    images=Image.objects.all()
    return render(request, 'home.html', )