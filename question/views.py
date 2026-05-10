from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from tag.models import Tag
from answer.models import Answer
from vote.models import Vote
from django.db.models import Count, Q
from django.contrib.admin.views.decorators import staff_member_required
from .forms import QuestionForm



@login_required
def create_question(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.auteur = request.user
            question.save()
            form.save_m2m()  # IMPORTANT pour tags

            return redirect('home')

    else:
        form = QuestionForm()

    return render(request, 'questions/create.html', {
        'form': form,
        'tags': form.fields['tags'].queryset
    })



def question_detail(request, id):
    question = get_object_or_404(Question, id=id)

    question.views += 1
    question.save()

    answers = question.answers.select_related('auteur').annotate(
        upvotes=Count('votes', filter=Q(votes__type_vote="up")),
        downvotes=Count('votes', filter=Q(votes__type_vote="down")),
    )

    question.upvotes = question.votes.filter(type_vote="up").count()
    question.downvotes = question.votes.filter(type_vote="down").count()

    return render(request, "questions/detail.html", {
        "question": question,
        "answers": answers,
    })

@login_required
def vote_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    vote_type = request.POST.get("type_vote", "up")

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

    return redirect('question_detail', id=pk)


@staff_member_required
def manage_questions(request):
    questions = Question.objects.all()
    return render(request, "admin/gestion_questions.html", {
        "questions": questions
    })

@staff_member_required
def delete_question(request, id):
    question = get_object_or_404(Question, id=id)
    question.delete()
    return redirect("manage_questions")

@login_required
def delete_own_question(request, id):
    question = get_object_or_404(Question, id=id)

    if request.user == question.auteur:
        question.delete()

    return redirect("profile")

