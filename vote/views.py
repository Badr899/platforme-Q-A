from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vote
from question.models import Question
from answer.models import Answer



@login_required
def vote_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    vote_type = request.POST.get("type_vote")

    if vote_type not in ["up", "down"]:
        return redirect("question_detail", id=pk)

    vote = Vote.objects.filter(user=request.user, question=question).first()

    if vote:
        if vote.type_vote == vote_type:
            vote.delete()
        else:
            vote.type_vote = vote_type
            vote.save()
    else:
        Vote.objects.create(
            user=request.user,
            question=question,
            type_vote=vote_type
        )

    return redirect("question_detail", id=pk)


@login_required
def vote_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)

    vote_type = request.POST.get("type_vote")  # 🔥 IMPORTANT

    vote = Vote.objects.filter(user=request.user, answer=answer).first()

    if vote:
        if vote.type_vote == vote_type:
            vote.delete()
        else:
            vote.type_vote = vote_type
            vote.save()
    else:
        Vote.objects.create(
            user=request.user,
            answer=answer,
            type_vote=vote_type
        )

    return redirect("question_detail", id=answer.question.id)