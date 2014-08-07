from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'job_runner.views.home', name='home'),
    # url(r'^job_runner/', include('job_runner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^runner/', include('runner.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^$', 'job_runner.views.home', name='home'),
)
