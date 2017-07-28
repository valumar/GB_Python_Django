from django.db import models


class Work(models.Model):
    years = models.CharField(max_length=10)
    place = models.CharField(max_length=32)
    position = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.id}. {self.place}'


class Education(models.Model):
    years = models.CharField(max_length=10)
    place = models.CharField(max_length=32)
    position = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.id}. {self.place}'
