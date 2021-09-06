from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



class File(models.Model):
    file = models.ForeignKey(User, on_delete=models.CASCADE)
    file_real = models.FileField()


3