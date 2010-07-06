from django.conf.urls.defaults import *


urlpatterns = patterns('work.views',
   url(r'^$', 'project_list', name="project_index"),
)
