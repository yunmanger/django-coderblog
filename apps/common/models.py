from django.db import models


class Link(models.Model):
    title       = models.CharField(max_length=50)
    url         = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_public   = models.BooleanField(default=True)
    order       = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'%s' % self.title
