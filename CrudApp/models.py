from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
# Create your models here.
class StudentModels(models.Model):
    id = models.AutoField(primary_key=True)
    Name =  models.CharField(max_length=50)
    Father_Name =  models.CharField(max_length=50)
    Mother_Name =  models.CharField(max_length=50)
    Age =  models.IntegerField()
    College_Name =  models.CharField(max_length=100)
    Department =  models.CharField(max_length=20)
    Address =  models.CharField(max_length=200)
    Phone_Number =  models.IntegerField()
    Email =  models.EmailField(max_length=20)
    Upload_images =  models.ImageField(upload_to="images/")



@receiver(post_delete, sender=StudentModels)
def _post_image_file(sender, instance, **kwargs):
    if instance.Upload_images:
        if os.path.isfile(instance.Upload_images.path):
            os.remove(instance.Upload_images.path)
    



