from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import Gallery, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 5


class GalleryAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links', 'date', 'modified', 'public')
    search_fields = ('title', 'description')
    list_filter = ('public',)
    ordering = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]

admin.site.register(Gallery, GalleryAdmin)