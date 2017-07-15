from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from website.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^project$', project, name='project'),
    url(r'^sub_project/(?P<name>[a-zA-Z0-9_]+)$', sub_project, name='sub_project'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
