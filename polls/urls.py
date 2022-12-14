from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),            #ex: /polls/5/
    path('results/<int:question_id>/', views.results, name="results"),  #ex: /polls/results/5/
    path('vote/<int:question_id>/', views.vote, name="index"),          #ex: /polls/votes/5/
    
]