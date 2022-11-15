from django.shortcuts import render, HttpResponse

# Create your views here
recipes = [
    {
        'author': 'Armo',
        'title': 'meatball',
    },
    {
        'author': 'Carlo',
        'title': 'spaghetti',
    },
]


def home(request):
    context = {
        'recipes': recipes,
    }
    return render(request, "recipes/home.html", context=context)


def about(request):
    return render(request, "recipes/about.html", {'title': 'About'})
