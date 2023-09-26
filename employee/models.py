from django.db import models

# Create your models here.

class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images",max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"