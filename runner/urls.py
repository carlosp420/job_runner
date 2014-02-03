from django.conf.urls import patterns, include, url

from runner.views import index

urlpatterns = patterns('',
        url(r'^$', index)
)
