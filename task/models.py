from django.db import models


class Border(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)
    borders = models.ManyToManyField(Border)


class CountryDetails(models.Model):
    name = models.CharField(max_length=255)
    alpha2code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    population = models.IntegerField()
    timezone = models.DateTimeField(auto_now=True)
    flag = models.ImageField(upload_to='', null=True)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')
    borders = models.ManyToManyField(Border)


class GetData(models.Model):
    name = models.CharField(max_length=255)
    alpha2code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)

