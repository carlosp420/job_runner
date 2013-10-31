from django.conf.urls import patterns, include, url

from status.views import index

urlpatterns = patterns('',
        url(r'^$', index),
)
