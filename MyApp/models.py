from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=15)
    Course = models.CharField(max_length=200)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name