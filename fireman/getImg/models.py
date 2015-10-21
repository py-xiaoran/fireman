from django.db import models

# Create your models here.

class ImageType(models.Model):
    type_name = models.TextField(max_length=20)

class ImageSrc(models.Model):
    img_name = models.TextField(max_length=50)
    img_local = models.TextField(max_length=255)
    img_type = models.ForeignKey(ImageType)
    

