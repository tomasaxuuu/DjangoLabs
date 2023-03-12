from django.db import models


class Model(models.Model):
    latitude = models.IntegerField('Широта')
    longitude = models.IntegerField('Долгота')
    temperature = models.IntegerField('Температура')
    data_and_time = models.DateTimeField('Дата и время')

    def __str__(self):
        return f'Запись №{self.latitude}'

    def get_absolute_url(self):
        return f'/laboratory_six'
