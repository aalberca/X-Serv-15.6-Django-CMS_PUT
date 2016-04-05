from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^cms/$', 'cms_put.views.muestra_todo'),
    url(r'^cms/(\d+)', 'cms_put.views.pagina'),
    url(r'^cms/(.+)/(.*)', 'cms_put.views.nueva_pagina'),
    url(r'^admin/', include(admin.site.urls)),
)
