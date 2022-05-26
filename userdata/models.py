from django.db import models

# Create your models here.

class Userdata(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    username = models.CharField(max_length=70,blank=False, default='')
    age = models.IntegerField(default=0)
    dob = models.DateTimeField(auto_now=True)

