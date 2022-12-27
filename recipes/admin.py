from django.contrib import admin
from . import models

class RecipeIngredientInLine(admin.TabularInline):
    model = models.RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    extra = 0
    readonly_fields = ['created_at', 'updated_at']


# Register your models here.
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Unit)
admin.site.register(models.Ingredient)
