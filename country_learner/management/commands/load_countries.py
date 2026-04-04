import csv
from django.core.management.base import BaseCommand
from country_learner.models import Country


class Command(BaseCommand):
    help = 'Load countries from CSV file'

    def handle(self, *args, **kwargs):
        with open('countries.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                Country.objects.create(
                    name=row['name'],
                    capital=row['capital'],
                    square=row['square'],
                    population=row['population'],
                    world_part=row['part']
                )

        self.stdout.write(self.style.SUCCESS('Countries loaded successfully'))