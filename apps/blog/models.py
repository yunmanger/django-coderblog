from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title       = models.CharField(max_length=25)
    slug        = models.SlugField(max_length=35, unique=True)
    
    def __unicode__(self):
        return u'%s' % self.title

class Post(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=100)
    category    = models.ForeignKey(Category)
    text        = models.TextField()
    markup      = models.CharField(editable=False, default='htm', max_length=3)
    pub_date    = models.DateTimeField()
    mod_date    = models.DateTimeField()
    
    def __unicode__(self):
        return u'%s' % self.title
