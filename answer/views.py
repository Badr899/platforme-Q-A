from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Answer
from question.models import Question
from vote.models import Vote
from django.shortcuts import render
from .models import Answer
from django.db.models import Count, Q




@login_required
def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        Answer.objects.create(
            contenu=request.POST["contenu"],
            auteur=request.user,
            question=question
        )

    return redirect("question_detail", id=question_id)


@login_required
def accept_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)

    if request.user != answer.question.auteur:
        return redirect("question_detail", pk=answer.question.id)

    answer.question.answers.update(est_acceptee=False)
    answer.est_acceptee = True
    answer.save()

    return redirect("question_detail", pk=answer.question.id)



def answers_list(request):
    answers = Answer.objects.select_related("question", "auteur").annotate(
        upvotes=Count('votes', filter=Q(votes__type_vote="up")),
        downvotes=Count('votes', filter=Q(votes__type_vote="down")),
    ).order_by("-date_creation")

    # 🔥 score calculé ici
    for a in answers:
        a.score = a.upvotes - a.downvotes

    return render(request, "answers/answers_list.html", {
        "answers": answers
    })







@staff_member_required
def manage_answers(request):
    answers = Answer.objects.select_related('auteur', 'question').all().order_by('-id')

    return render(request, "admin/manage_reponses.html", {
        "answers": answers
    })


@login_required
def delete_answer(request, id):
    if request.method != "POST":
        return redirect("home")

    answer = get_object_or_404(Answer, id=id)

    # ✅ sécurité : admin OU auteur
    if request.user == answer.auteur or request.user.is_staff:
        question_id = answer.question.id
        answer.delete()
        return redirect("question_detail", id=question_id)

