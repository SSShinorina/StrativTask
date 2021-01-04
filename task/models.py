from django.db import models


# Create your models here.name, alphacode2, capital, population, timezone, flag, languages and neighbouring
# countries.


class Border(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)
    borders = models.ManyToManyField(Border)


class Details(models.Model):
    name = models.CharField(max_length=255)
    alpha2code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    population = models.IntegerField()
    timezone = models.DateTimeField(auto_now=True)
    flag = models.ImageField(upload_to='', null=True)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')
    borders = models.ManyToManyField(Border)

#
# class Speak_language(models.Model):
#     name = models.ManyToManyField(Language)
#     border = models.ManyToManyField(Border)


class Get(models.Model):
    name = models.CharField(max_length=255)
    alpha2code = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    population = models.IntegerField()
    timezone = models.DateTimeField()
    flag = models.ImageField(upload_to='')
    languages = models.ForeignKey(Language, on_delete=models.CASCADE)
    borders = models.ManyToManyField(Border)
