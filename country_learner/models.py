from django.db import models

class Country(models.Model):
    """Model of country"""
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    square = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    world_part = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserCountry(models.Model):
    """Model of a country which can be added to the user's list"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name