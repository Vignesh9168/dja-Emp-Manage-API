from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    place =  models.CharField(max_length=50)
    email = models.EmailField(default='')
    password = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.name