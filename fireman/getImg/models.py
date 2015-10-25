from django.db import models

# Create your models here.
# id is primary key
class ImageType(models.Model):
    type_name = models.TextField(max_length=20)

#id is primary key
class ImageSrc(models.Model):
    img_name = models.TextField(max_length=50)
    img_local = models.TextField(max_length=255)
    img_type = models.ForeignKey(ImageType)
    img_weight = models.IntegerField()
    img_height = models.IntegerField()
    

