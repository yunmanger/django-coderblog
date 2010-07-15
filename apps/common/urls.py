from django.conf.urls.defaults import *


urlpatterns = patterns('common.views',
   url(r'^ping/google/$', 'ping', name="ping_google"),
   url(r'^ping/url/$', 'ping_url', name="ping_url"),
   url(r'^dtw/$', 'dtw', name="twitter_download"),
   url(r'^twitter/post/$', 'ptw', name="twitter_post"),
)
