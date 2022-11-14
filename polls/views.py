from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")
