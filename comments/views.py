from tokenize import Comment

from django.shortcuts import render

# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from answer.models import Answer
from .models import Comments

@login_required
def add_comment_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == "POST":
        contenu = request.POST.get("contenu")

        if contenu:
            Comments.objects.create(
                contenu=contenu,
                auteur=request.user,
                answer=answer
            )

    return redirect("question_detail", id=answer.question.id)



@staff_member_required
def manage_comments(request):
    comments = Comments.objects.select_related('auteur', 'answer').all().order_by('-id')

    return render(request, "admin/manage_comment.html", {
        "comments": comments
    })

@login_required
def delete_comment(request, id):
    if request.method != "POST":
        return redirect("home")

    comment = get_object_or_404(Comments, id=id)

    # sécurité : admin OU auteur
    if request.user == comment.auteur or request.user.is_staff:

        # ✅ SAFE CHECK
        question_id = None

        if comment.answer and comment.answer.question:
            question_id = comment.answer.question.id

        comment.delete()

        if question_id:
            return redirect("question_detail", id=question_id)

        return redirect("home")

    return redirect("home")