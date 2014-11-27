from django.conf.urls import patterns, include, url
from django.contrib import admin
import cowpti
import cowpti2
from cowpti2 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cowpti.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^upload$', cowpti2.views.upload_file)
)
