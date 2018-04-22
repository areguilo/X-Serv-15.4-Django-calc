from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'calc.views.barra'),
    url(r'^(\-?\d+)\+(\-?\d+)','calc.views.suma'),
    url(r'^(\-?\d+)\-(\-?\d+)','calc.views.resta'),
    url(r'^(\-?\d+)\.(\-?\d+)','calc.views.multiplicacion'),
    url(r'^(\-?\d+)\/(\-?\d+)','calc.views.division'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.+','calc.views.error'),
)
