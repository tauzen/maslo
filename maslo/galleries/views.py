from django.views.generic import ListView
from .models import Gallery


class GalleryList(ListView):
    model = Gallery