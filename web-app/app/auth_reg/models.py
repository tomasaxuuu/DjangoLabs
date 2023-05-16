from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class User(AbstractUser):
    user_role = models.CharField('user_role', max_length=200, default='user')


class Longitude(models.Model):
    longitude = models.IntegerField('Долгота')

    def __str__(self):
        return f'{self.longitude}'


class Latitude(models.Model):
    latitude = models.IntegerField('Широта')

    def __str__(self):
        return f'{self.latitude}'


class City(models.Model):
    latitude = models.OneToOneField(Latitude, on_delete=models.CASCADE)
    longitude = models.OneToOneField(Longitude, on_delete=models.CASCADE)
    city = models.CharField('Город', max_length=20)

    def __str__(self):
        return f'{self.city}'


class Device(models.Model):
    device = models.CharField('Оборудование', max_length=20)

    def __str__(self):
        return f'{self.device}'


class Measurements(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # longitude = models.ForeignKey(City, on_delete=models.CASCADE)
    # latitude = models.ForeignKey(City, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    device = models.ManyToManyField(Device)
    temperature = models.FloatField("Температура", max_length=6)
    def __str__(self):
        return f'Измерение №{self.id}'