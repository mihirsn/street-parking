from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12, unique = True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
