from django.db import models

# Create your models here.
class Student(models.Model):
    title = models.IntegerField()
    content = models.TextField()
    creaded_by = models.CharField(max_length=66)
    