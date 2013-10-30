from django.db import models

# File uploader
class Uploader(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
