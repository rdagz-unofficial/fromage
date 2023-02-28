from django.shortcuts import render
from .models import Cheese, Review

# Create your views here.

def home(request):

    context = {
        "cheeses": Cheese.objects.all(),
        "reviews": Review.objects.filter(recommend=True)
    }

    return render(request, "catalogue/home.html", context)
