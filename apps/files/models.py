from django.db import models
from django.contrib.auth.models import User

import os

class File(models.Model):
    def specific_dir(self, filename):
        return "files/uploads/%s/%s" % (self.user.username, filename)
    user = models.ForeignKey(User)
    file = models.FileField(upload_to=specific_dir)
    
    def get_filename(self):
        return os.path.basename(self.file.name)
        
    def link(self):
        return self.file.url
        
    def __unicode__(self):
        return u"%s" % self.file.name