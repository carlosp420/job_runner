from django.conf.urls import patterns, include, url

from runner.views import index, software

urlpatterns = patterns('',
        url(r'^$', index),
        url(r'^software/(?P<name>[A-Za-z]+_\d\.\d\.*\d*)/$', software),
)
