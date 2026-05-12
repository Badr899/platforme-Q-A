from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_question, name='create_question'),
    path("<int:id>/", views.question_detail, name="question_detail"),
    path('admin/questions/', views.manage_questions, name='manage_questions'),
    path('admin/questions/delete/<int:id>/', views.delete_question, name='delete_question'),
    path('questions/delete/<int:id>/', views.delete_own_question, name='delete_own_question'),

]