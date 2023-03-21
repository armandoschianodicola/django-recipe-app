from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from rest_framework import generics, permissions

from . import models
from . import serializers


def home(request):

    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, "recipes/home.html", context=context)


class RecipeView(generics.CreateAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class RecipeAPIListView(generics.ListAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class RecipeDetailView(DetailView):
    model = models.Recipe

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        recipe_ingredient_formset = modelformset_factory(
            models.RecipeIngredient,
            fields=('ingredient', 'quantity', 'unit'),
            extra=2
            )
        context['formset'] = recipe_ingredient_formset(queryset=self.object.recipeingredient_set.all())

        return context


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title']

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        recipe_ingredient_formset = modelformset_factory(
            models.RecipeIngredient,
            fields=('ingredient', 'quantity', 'unit'),
            extra=2
            )
        context['formset'] = recipe_ingredient_formset(queryset=self.object.recipeingredient_set.all())

        return context


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = models.Ingredient
    fields = ['name']


def about(request):
    return render(request, "recipes/about.html", {'title': 'About'})
