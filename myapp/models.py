from django.db import models

# Dentro de models.py

class Course(models.Model):
    idcourse = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    hour = models.IntegerField()
    credits = models.IntegerField()
    state = models.BooleanField(default=True)

class Career(models.Model):
    idcareer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=90)
    image = models.ImageField(default='null')
    state = models.BooleanField(default=True)
