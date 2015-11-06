from bolt.views import IndexView
from django.conf.urls import patterns, include, url
from django.contrib import admin

from athletes import api_urls as athletes_api_url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bolt.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),

                       # API 1.0
                       url(r'^api/1.0/', include(athletes_api_url)),
                       )
