from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Recipe(TimeStampedModel, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('recipes-detail', kwargs={'pk': self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
