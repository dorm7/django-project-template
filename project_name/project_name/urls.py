from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django_kss.views import AutoStyleGuideView
import django_kss.urls

admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    url(r'^$', TemplateView.as_view(template_name='base.html')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^style_guide/', include(django_kss.urls)),
)
