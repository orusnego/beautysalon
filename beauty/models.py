from django.db import models
from django.contrib.auth.models import User



class typeBeauty(models.Model):
    type = models.CharField(max_length=40)
    image = models.ImageField(upload_to='beauty/images/types', blank=True)
    def __str__(self):
        return self.type

class Beauty(models.Model):
    procedures = models.ForeignKey(typeBeauty, on_delete=models.CASCADE, default=1, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='beauty/images/uslugi')
    def __str__(self):
        return self.title



# Create your models here.
