from django.db import models

# Create your models here.


class User(models.Model):
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField
    insta = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    github = models.CharField(max_length=200)


class Project(models.Model):
    p = models.TextField()
