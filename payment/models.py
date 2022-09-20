from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()

    @staticmethod
    def get_absolute_url():
        return reverse('items')

    def __str__(self):
        return self.name
