from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from galleries.views import GalleryList, GalleryDetail
from contact.views import ContactFormView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^gallery/$', GalleryList.as_view()),
    url(r'^gallery/(?P<slug>[A-Za-z0-9_\-]+)/$', GalleryDetail.as_view()),
    url(r'^contact/$', ContactFormView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
