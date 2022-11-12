from django.shortcuts import render, HttpResponse

# Create your views here


def home(request):
    return HttpResponse('Recipes Home')


def about(request):
    return HttpResponse('About')
