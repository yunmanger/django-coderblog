from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
   url(r'^$', 'post_list', name="post_list"),
)
