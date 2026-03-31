from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    square = models.DecimalField(max_digits=10, decimal_places=2)
    population = models.IntegerField()
    flag = models.URLField()

    def __str__(self):
        return self.name