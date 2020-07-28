from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def clean_s1(s1):
    print("hello "+s1)
    print(type(s1))
    for x in s1:
        if not (x=='1' or x=='0'):
            raise ValidationError("ONLY BINARY NUMBER")

class con(models.Model):
    s1=models.CharField(max_length=100,validators=[clean_s1])


class dec(models.Model):
    s1=models.IntegerField()
