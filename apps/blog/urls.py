#coding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view='post_detail',
        name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/yvi/$',
        view='post_on_yvi',
        name='blog_post_on_yvi'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        view='post_archive',
        name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        view='post_archive',
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        view='post_archive',
        name='blog_archive_year'
    ),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        view='category_detail',
        name='blog_category_detail'
    ),
    url (r'^categories/$',
        view='category_list',
        name='blog_category_list'
    ),
#    url(r'^tags/(?P<slug>[-\w]+)/$',
#        view='tag_detail',
#        name='blog_tag_detail'
#    ),
#    url (r'^search/$',
#        view='search',
#        name='blog_search'
#    ),
    url(r'^page/(?P<page>\w)/$',
        view='post_list',
        name='blog_index_paginated'
    ),
    url(r'^$',
        view='post_list',
        name='blog_index'
    ),
)

from blog.feeds import BlogPostsFeed, BlogPostsByCategory

urlpatterns += patterns('',
    url(r'^feed/$', view=BlogPostsFeed(), name="blog_index_feed"),
    url(r'^feed/(?P<slug>[-\w]+)/$', view=BlogPostsByCategory(), name="blog_category_feed"),
)
