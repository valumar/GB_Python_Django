from django.db import models
from django.template import defaultfilters
from unidecode import unidecode


class Organization(models.Model):
    name = models.CharField(verbose_name='Название', max_length=48)
    region = models.CharField(verbose_name='Регион', max_length=32)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = defaultfilters.slugify(unidecode(self.name))
            super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация', null=False)
    years = models.CharField(max_length=10)
    # place = models.CharField(max_length=32)
    position = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.id}. {self.organization.name}'


class Education(models.Model):
    years = models.CharField(max_length=10)
    place = models.CharField(max_length=32)
    position = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.id}. {self.place}'
