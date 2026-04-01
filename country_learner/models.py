from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    square = models.IntegerField()
    population = models.IntegerField()

    def __str__(self):
        return self.name


class UserCountry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name