# -*- coding: utf-8 -*-
import os
from django.db import models
from model_utils.models import TimeStampedModel
from adminsortable.models import Sortable
from settings.base import MEDIA_ROOT


class Gallery(TimeStampedModel, Sortable):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    public = models.BooleanField(default=False)
    description = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def get_cover_photo(self):
        photo = Photo.objects.filter(gallery=self).get(is_cover_photo=True)
        return photo.image.name

    class Meta(Sortable.Meta):
        verbose_name_plural = "galleries"


class Photo(TimeStampedModel, Sortable):
    image = models.ImageField(upload_to='photos/%Y/%m')
    gallery = models.ForeignKey(Gallery)
    is_cover_photo = models.BooleanField()

    def __unicode__(self):
        return self.image.name

    def save(self):
        if self.is_cover_photo:
            previous_cover_photos = Photo.objects.filter(gallery=self.gallery, is_cover_photo=True)
            for photo in previous_cover_photos:
                photo.is_cover_photo = False
                photo.save()
        super(Photo, self).save()

    def delete(self):
        try:
            os.remove(MEDIA_ROOT + self.image.name)
        except IOError:
            pass
        super(Photo, self).delete()

    class Meta(Sortable.Meta):
        pass
