from django.conf.urls.defaults import *


urlpatterns = patterns('work.views',
   url(r'^$', 'project_list', name="project_index"),
   url(r'^(?P<slug>[-\w]+)/$', 'project_detail', name="project_detail"),
   url(r'^(?P<slug>[-\w]+)/todos/$', 'todo_list', name="project_todos"),
)
