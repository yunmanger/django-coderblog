from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

from blog.utils import post_to_yvi
from tagging.fields import TagField

POST_VISIBILITY = (
     (1, "everywhere"),
     (2, "projects"),
)

class Category(models.Model):
    title       = models.CharField(max_length=25)
    slug        = models.SlugField(max_length=35, unique=True)

    @models.permalink
    def link(self):
        return ('blog_category_detail',(),{'slug': self.slug})

    def get_absolute_url(self):
        return self.link()
    
    def __unicode__(self):
        return u'%s' % self.title
    
class PublicManager(models.Manager):
    
    def published(self):
        now = datetime.datetime.now()
        return self.get_query_set().filter(pub_date__lte=now, visibility=1)

class Post(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(max_length=120)
    category    = models.ForeignKey(Category)
    text        = models.TextField()
    markup      = models.CharField(editable=False, default='mrk', max_length=3)
    pub_date    = models.DateTimeField()
    mod_date    = models.DateTimeField()
    visibility  = models.IntegerField(choices=POST_VISIBILITY, default=1)
    tags        = TagField(default='')
    objects     = PublicManager()
    
    class Meta:
        ordering = ['-pub_date']
    
    @models.permalink
    def link(self):
        d = self.pub_date
        return ('blog_detail',(),{'year':d.year,'month': d.strftime("%m"),'day':d.strftime("%d"),'slug': self.slug})
    
    def get_absolute_url(self):
        return self.link()
    
    def post_on_yvi(self):
        if settings.YVI_ENABLED:
            post_to_yvi(self)
    
    def __unicode__(self):
        return u'%s' % self.title
