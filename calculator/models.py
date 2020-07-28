from django.db import models

# Create your models here.
class Calculate(models.Model):
    n1 = models.DecimalField(max_digits=20,decimal_places=10)
    n2 = models.DecimalField(max_digits=20,decimal_places=10)
