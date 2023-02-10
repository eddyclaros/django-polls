from . import views
from django.urls import path

app_name = "polls"

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name="index"),
    #path('<int:question_id>/', views.detail, name="detail"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),             #ex: /polls/5/
    #path('results/<int:question_id>/', views.results, name="results"),  #ex: /polls/results/5/
    path('results/<int:pk>/', views.ResultView.as_view(), name="results"),
    path('vote/<int:question_id>/', views.vote, name="vote"),          #ex: /polls/votes/5/
    
]