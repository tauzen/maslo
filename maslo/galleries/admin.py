from django.contrib import admin
from .models import Gallery, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 5


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'modified', 'public')
    search_fields = ('title', 'description')
    list_filter = ('public',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]

admin.site.register(Gallery, GalleryAdmin)