from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from django.contrib.admin.views.decorators import staff_member_required
from .forms import QuestionForm
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render
from .models import Question




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

    # 🔥 incrément views (OK mais mieux en update)
    question.views += 1
    question.save(update_fields=["views"])

    # 🔥 votes question (OPTIMISÉ)
    question.upvotes = question.votes.filter(type_vote="up").count()
    question.downvotes = question.votes.filter(type_vote="down").count()
    question.score = question.upvotes - question.downvotes

    # 🔥 answers avec votes (BON)
    answers = question.answers.select_related('auteur').annotate(
        upvotes=Count('votes', filter=Q(votes__type_vote="up")),
        downvotes=Count('votes', filter=Q(votes__type_vote="down")),
    )

    return render(request, "questions/detail.html", {
        "question": question,
        "answers": answers,
    })




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

