from django.conf.urls.defaults import *


urlpatterns = patterns('common.views',
   url(r'^ping/$', 'ping', name="ping_google"),
   url(r'^dtw/$', 'dtw', name="twitter_download"),
   url(r'^twitter/post/$', 'ptw', name="twitter_post"),
)
