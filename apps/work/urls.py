from django.conf.urls.defaults import *


urlpatterns = patterns('work.views',
   url(r'^$', 'project_list', name="project_index"),
   url(r'^(?P<slug>[-\w]+)/$', 'project_detail', name="project_detail"),
   url(r'^(?P<slug>[-\w]+)/todos/$', 'todo_list', name="project_todos"),
   url(r'^(?P<slug>[-\w]+)/todos/(?P<id>\d+)/$', 'todo_detail', name="project_todo_detail"),
   url(r'^(?P<slug>[-\w]+)/todos/(?P<id>\d+)/edit/$', 'todo_form', name="project_todo_edit"),
   url(r'^(?P<slug>[-\w]+)/todos/new/$', 'todo_form', name="project_todo_new"),
   url(r'^(?P<slug>[-\w]+)/posts/$', 'post_list', name="project_posts"),
   url(r'^(?P<slug>[-\w]+)/posts/(?P<id>\d+)/$', 'post_detail', name="project_post_detail"),
)
