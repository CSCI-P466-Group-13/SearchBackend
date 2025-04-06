from django.db import models

# Create your models here.
class car(models.Model):
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    trim = models.CharField(max_length=30)
    mileage = models.CharField(max_length=7)
    year = models.IntegerField()
    price = models.CharField(max_length=7)
    description = models.TextField()
    name = models.TextField()
    drivetrain = models.CharField(max_length=25)

class property(models.Model):
    price = models.IntegerField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_zip = models.CharField(max_length=25)
    country = models.CharField(max_length=10)
    square_feet = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    lot_size = models.IntegerField()
    year_built = models.IntegerField()
    year_renovated = models.IntegerField()
