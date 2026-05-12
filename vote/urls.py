from django.urls import path
from . import views

urlpatterns = [
    path("question/<int:pk>/vote/", views.vote_question, name="vote_question"),
            path('answer/<int:pk>/', views.vote_answer, name='vote_answer'),
]