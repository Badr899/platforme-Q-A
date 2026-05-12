from django.urls import path
from . import views

urlpatterns = [
    path("", views.answers_list, name="answers_list"),
    path("question/<int:question_id>/answer/", views.create_answer,name="create_answer"),
    path( "accept/<int:pk>/",views.accept_answer,name="accept_answer"),
    
    path('admin/answers/', views.manage_answers, name='manage_answers'),
    path('admin/answers/delete/<int:id>/', views.delete_answer, name='delete_answer'),

]