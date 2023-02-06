from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice



# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html",{"latest_question_list":latest_question_list})
    #return HttpResponse("Estas en la página principal de premios platzy")


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html",{
        "question":question
    })

    #return HttpResponse(f"Estás viendo la pregunta numero {question_id}")


def results(request,question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta numero {question_id}")


def vote(request,question_id):
    return HttpResponse(f"Estás votando a la pregunta numero {question_id}")


# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """ return the last five published questions """
#         return Question.objects.filter("-pub_date")[:5]

