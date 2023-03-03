from django.db import models
from django.contrib.auth.models import User
from beauty.models import Beauty, typeBeauty

class Master(models.Model):
    name = models.CharField(max_length=100)
    profession = models.ForeignKey(typeBeauty,on_delete=models.CASCADE)
    experience = models.IntegerField()
    image = models.ImageField(upload_to='masters/images')
    description = models.TextField(max_length=1000, blank=True)
    url = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name
            
class Review(models.Model):
    five = '5'
    four = '4'
    three = '3'
    two = '2'
    one = '1'
    rate_choises = [
        (five, '5'),
        (four,'4'),
        (three, '3'),
        (two,'2'),
        (one,'1')
    ]
    text = models.CharField(max_length=10000, verbose_name='Отзыв')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    master = models.ForeignKey(Master,on_delete=models.CASCADE)
    rate = models.CharField(max_length=1,choices=rate_choises, verbose_name='Оцените мастера')
    name = models.CharField(max_length=50, default='Аноним', verbose_name='Введите свое имя')
    def __str__(self):
        return self.text

class Work(models.Model):
    master = models.ForeignKey(Master,on_delete=models.CASCADE, default=1)
    procedure = models.ForeignKey(Beauty,on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='works/images')    

# Create your models here.
