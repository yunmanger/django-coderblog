from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

from tagging.fields import TagField

import datetime

TODO_CHOICES = (
    (1, "Mondatory"),
    (2, "Required"),
    (3, "Optional"),
    (4, "Fuzzy"),
)

TODO_STATUS = (
    (1, "new"),
    (2, "in process"),
    (3, "done"),
    (4, "fuzzy"),
)

class PublicManager(models.Manager):
    
    def published(self):
        now = datetime.datetime.now()
        return self.get_query_set().filter(is_public=True, pub_date__lte=now)

class Project(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=60, unique=True)
    desc_ref    = models.CharField(max_length=128, blank=True, null=True)
    pub_date    = models.DateTimeField()
    is_public   = models.BooleanField(default=True)
    tags        = TagField()
    objects     = PublicManager()

    @models.permalink
    def link(self):
        return ('project_detail',(),{'slug': self.slug })

    def get_absolute_url(self):
        return self.link()
    
    def __unicode__(self):
        return self.title
    
    
class Todo(models.Model):
    user        = models.ForeignKey(User)
    project     = models.ForeignKey(Project)
    title       = models.CharField(max_length=128)
    desc        = models.TextField()
    type        = models.IntegerField(choices=TODO_CHOICES)
    status      = models.IntegerField(choices=TODO_STATUS, default=1)
    pub_date    = models.DateTimeField()
    deadline    = models.DateTimeField(null=True, blank=True)
    is_public   = models.BooleanField(default=True)
    objects     = PublicManager()

    def __unicode__(self):
        return self.title
