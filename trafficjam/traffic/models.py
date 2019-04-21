from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# ------ For Post_create -------
class postcreate(models.Model):
    name = models.ForeignKey(User, default=None, on_delete='')
    place_name = models.CharField(max_length=200,default='')
    #image = models.ImageField(default='')
    trafficjam_details = models.TextField(max_length=900,default='')
    date_and_time = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name_plural = " Post_create "

# ------- For weather -------
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Weather'

# ------ For Contact -------
class Contact(models.Model):
    name = models.ForeignKey(User, default=None, on_delete='')
    email = models.EmailField(max_length=100,default='')
    message = models.TextField(max_length=900,default='')


    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = " Contact "

# ------ For Comment -------
class Comment(models.Model):
    name = models.ForeignKey(User, default=None, on_delete='')
    comment = models.TextField(max_length=900,default='')
    date_and_time = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "Comment"

