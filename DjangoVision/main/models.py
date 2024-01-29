from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_units = models.IntegerField()

    def __str__(self):
        return self.name