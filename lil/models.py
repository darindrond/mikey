from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    DOB=models.DateField()
    Mark=models.IntegerField()

