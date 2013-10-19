from django.views.generic import ListView, DetailView
from .models import Gallery, Photo


class GalleryList(ListView):
    model = Gallery


class GalleryDetail(DetailView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.filter(gallery=self.get_object())
        return context