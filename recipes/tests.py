from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Recipe, RecipeIngredient, Ingredient, Unit

User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user('test', password="test123")

    def test_user_pwd(self):

        is_checked = self.user_1.check_password('test123')
        self.assertTrue(is_checked)


class RecipeTestCase(TestCase):

        def setUp(self):
            self.user_1 = User.objects.create_user('test', password="test123")
            self.unit_1 = Unit.objects.create(
                name='kilo')
            self.recipe_1 = Recipe.objects.create(
                title='pasta al forno',
                author=self.user_1
            )
            self.recipe_2 = Recipe.objects.create(
                title='spaghetti alle vongole',
                author=self.user_1
            )
            self.ingredient_1 = Ingredient.objects.create(
                name='Vongole',
            )
            self.recipe_ingredient_1 = RecipeIngredient.objects.create(
                recipe=self.recipe_2,
                ingredient=self.ingredient_1,
                unit=self.unit_1,
                quantity=1,
            )

        def test_user_recipe_reverse_count(self):
            qs = self.user_1.recipe_set.all()
            self.assertEqual(qs.count(), 2)

        def test_user_recipe_forward_count(self):
            qs = Recipe.objects.filter(author=self.user_1)
            self.assertEqual(qs.count(), 2)

        def test_recipe_ingredient_reverse_count(self):
            qs_1 = self.recipe_1.recipeingredient_set.all()
            self.assertEqual(qs_1.count(), 0)
            qs_2 = self.recipe_2.recipeingredient_set.all()
            self.assertEqual(qs_2.count(), 1)

        def test_recipe_ingredient_forward_count(self):
            qs_1 = RecipeIngredient.objects.filter(recipe=self.recipe_1)
            self.assertEqual(qs_1.count(), 0)
            qs_2 = RecipeIngredient.objects.filter(recipe=self.recipe_2)
            self.assertEqual(qs_2.count(), 1)

        def test_user_multiple_level_relation_reverse(self):
            qs = RecipeIngredient.objects.filter(recipe__author=self.user_1)
            self.assertEqual(qs.count(), 1)
        