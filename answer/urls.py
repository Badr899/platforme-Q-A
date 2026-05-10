from django.urls import path
from . import views

urlpatterns = [
    path("", views.answers_list, name="answers_list"),
    path("question/<int:question_id>/answer/", views.create_answer,name="create_answer"),
    path( "accept/<int:pk>/",views.accept_answer,name="accept_answer"),
    path("vote/answer/<int:answer_id>/", views.vote_answer, name="vote_answer"),
    path("answer/<int:answer_id>/comment/", views.add_comment_answer, name="add_comment_answer"),
    path('admin/answers/', views.manage_answers, name='manage_answers'),
    path('admin/answers/delete/<int:id>/', views.delete_answer, name='delete_answer'),

]