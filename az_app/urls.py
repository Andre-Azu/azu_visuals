
from django.urls import path, register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url('^$', views.all_images,name='home'),
    url('category/',views.category_images ,name = 'category_results'),
    path('category/<category>', views.view_category, name='view_category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 