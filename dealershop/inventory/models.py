from django.db import models
from django import forms

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    year = models.IntegerField(default=1900)

    def __str__(self):
        return f"{self.brand}_{self.model}_{self.color}_{self.year}"

    class Meta:
        ordering = ['-year']    # all 조회시 -year순으로(최신순,내림차순) 정렬함

class Inventory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    number = models.IntegerField(default=1900)