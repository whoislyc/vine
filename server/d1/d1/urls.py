from django.conf.urls import patterns, include, url
from d1.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^hi/$', hi),
    ('^$', hi),
    ('^time/$', time),
    ('^comment/$', comment_board),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^write/(\w{1,40})$', comment_board),
    # Examples:
    # url(r'^$', 'd1.views.home', name='home'),
    # url(r'^d1/', include('d1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^articles/comments/', include('django.contrib.comments.urls')),
)