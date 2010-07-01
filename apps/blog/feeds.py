#coding:utf-8
from django.contrib.syndication.feeds import FeedDoesNotExist
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from blog.models import Post, Category


class BlogPostsFeed(Feed):
    _site = Site.objects.get_current()
    title = u'%s фид' % _site.name
    link = "/"
    description = u'%s фид постов.' % _site.name
    description_template = "feeds/posts_description.html"

    def link(self):
        return reverse('blog_index')

    def items(self):
        return Post.objects.published()[:10]

    def item_pubdate(self, obj):
        return obj.pub_date


class BlogPostsByCategory(Feed):
    _site = Site.objects.get_current()
    title = u'%s фид постов по разделу' % _site.name
    description_template = "feeds/posts_description.html"

    def get_object(self, request, slug=None):
        return Category.objects.get(slug__iexact=slug)

    def link(self, obj):
        print obj
        if not obj:
            raise FeedDoesNotExist
        return obj.get_absolute_url()

    def description(self, obj):
        return u"Посты в разделе %s" % obj.title

    def items(self, obj):
        return obj.post_set.published()[:10]
