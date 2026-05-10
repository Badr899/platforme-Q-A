from django.urls import path
from .views import add_comment_answer, manage_comments, delete_comment

urlpatterns = [
    path("answer/<int:answer_id>/comment/", add_comment_answer, name="add_comment_answer"),
    path('admin/comments/', manage_comments, name='manage_comments'),
    path('delete/<int:id>/', delete_comment, name='delete_comment'),

]