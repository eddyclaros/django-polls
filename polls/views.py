from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Estas en la página principal de premios platzy")


def detail(request,question_id):
    return HttpResponse(f"Estás viendo la pregunta numero {question_id}")


def results(request,question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta numero {question_id}")


def vote(request,question_id):
    return HttpResponse(f"Estás votando a la pregunta numero {question_id}")

