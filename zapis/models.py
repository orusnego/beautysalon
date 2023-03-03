from django.db import models
from django.contrib.auth.models import User
from beauty.models import Beauty, typeBeauty
from masters.models import Master


class BookingDays(models.Model):
    days = models.CharField(max_length=10)
    def __str__(self):
        return self.days
        
class BookingSlots(models.Model):
    nine = '09:00'
    ten = '10:00'
    eleven = '11:00'
    twelve = '12:00'
    thirteen = '13:00'
    fourteen = '14:00'
    fifthteen = '15:00'
    sixteen = '16:00'
    seventeen = '17:00'
    eighteen = '18:00'
    nineteen = '19:00'
    twenty = '20:00'
    
    time_choises = [
        (nine, '09:00'),
        (ten, '10:00'),
        (eleven, '11:00'),
        (twelve, '12:00'),
        (thirteen, '13:00'),
        (fourteen, '14:00'),
        (fifthteen, '15:00'),
        (sixteen, '16:00'),
        (seventeen, '17:00'),
        (eighteen, '18:00'),
        (nineteen, '19:00'),
        (twenty, '20:00')
    ]

    start_time = models.CharField(max_length=10, choices=time_choises)

    def __str__(self):
        return str(self.start_time)

class BookingTime(models.Model):
    
    days = models.ForeignKey(BookingDays,on_delete=models.CASCADE, null=True)
    start_time = models.ForeignKey(BookingSlots,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.days) + '. ' + str(self.start_time)



class Appointment(models.Model):
    procedure = models.ForeignKey(Beauty, on_delete=models.CASCADE, null=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, null=True)
    time = models.ForeignKey(BookingTime,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, verbose_name='Введите свое имя')
    last_name = models.CharField(max_length=50, verbose_name='Введите свою фамилию')
    phone = models.CharField(max_length=50, verbose_name='Введите номер телефона без 8')

    def __str__(self):
        return self.first_name + '. ' + str(self.time)