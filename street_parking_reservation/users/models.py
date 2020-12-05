from django.db import models

class Users(models.Model):
    name = models.TextField()
    phone_number = models.CharField(max_length=12)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #categories = models.ManyToManyField('Category', related_name='posts')
