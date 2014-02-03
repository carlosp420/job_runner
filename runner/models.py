from django.db import models

# File uploader
class Uploader(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Software(models.Model):
    program = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    path    = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s|%s' % (self.program, self.version)
