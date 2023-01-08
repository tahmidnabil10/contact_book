from django.db import models

# Create your models here for Python Contact Book Project.
class Contact(models.Model):
    
    objects = models.Manager()
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField()
    ContactNumber = models.CharField(max_length=10)



