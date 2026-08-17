# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


# Car Make Model
# - Name
# - Description
# - Any other fields you would like to include
# - __str__ method

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # Optional additional field
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


# Car Model
# - Many-to-One relationship with CarMake
# - Name
# - Type with limited choices
# - Year between 2015 and 2023
# - Any other fields
# - __str__ method

class CarModel(models.Model):

    # Many CarModels can belong to one CarMake
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='car_models'
    )

    name = models.CharField(max_length=100)

    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('SPORTS', 'Sports'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('OTHER', 'Other'),
    ]

    type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default='SUV'
    )

    # Model year
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    # Optional additional fields
    description = models.TextField(blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name