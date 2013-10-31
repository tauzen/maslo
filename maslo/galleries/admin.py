from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableStackedInline
from .models import Gallery, Photo

class PhotoInline(SortableStackedInline):
    model = Photo
    extra = 5


class GalleryAdmin(SortableAdmin):
    list_display = ('title', 'order', 'date', 'modified', 'public')
    search_fields = ('title', 'description')
    list_filter = ('public',)
    ordering = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]

admin.site.register(Gallery, GalleryAdmin)