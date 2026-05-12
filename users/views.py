from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from .forms import RegisterForm
from .models import User
from question.models import Question
from tag.models import Tag
from answer.models import Answer
from vote.models import Vote






#Page d'inscription
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )

        print("USER CREATED:", user.email)

        return redirect('login')

    return render(request, 'users/register.html')

#Page de connexion
def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('home')

    return render(request, 'users/login.html')


#supprimer la session de l'utilisateur et rediriger vers la page de connexion
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    questions = Question.objects.all().order_by('-id')  # ou '-created_at'
    tags = Tag.objects.all()

    return render(request, "base/home.html", {
        "questions": questions,
        "tags": tags
    })


@staff_member_required
def admin_dashboard(request):
    context = {
        "tag_count": Tag.objects.count(),
        "question_count": Question.objects.count(),
        "user_count": User.objects.count(),
        "answer_count": Answer.objects.count(),

    }
    return render(request, "admin/admin_dashboard.html", context)

@login_required
def profile_view(request):
    user = request.user

    questions = Question.objects.filter(auteur=user)
    answers = Answer.objects.filter(auteur=user)

    # Votes reçus sur ses questions
    q_up = Vote.objects.filter(question__auteur=user, type_vote="up").count()
    q_down = Vote.objects.filter(question__auteur=user, type_vote="down").count()

    # Votes reçus sur ses réponses
    a_up = Vote.objects.filter(answer__auteur=user, type_vote="up").count()
    a_down = Vote.objects.filter(answer__auteur=user, type_vote="down").count()

    # Réputation
    reputation = (q_up + a_up) - (q_down + a_down)

    return render(request, "users/profile.html", {
        "questions": questions,
        "answers": answers,
        "upvotes": q_up ,
        "downvotes": q_down ,
        "a_up": a_up,
        "reputation": reputation,
    })




@staff_member_required
def manage_users(request):
    users = User.objects.all()
    return render(request, "admin/gestion_users.html", {
        "users": users
    })


@staff_member_required
def delete_user(request, id):
    if request.method != "POST":
        return redirect("manage_users")

    user = get_object_or_404(User, id=id)

    # protection super admin
    if user.is_superuser:
        return redirect("manage_users")

    # protection auto-delete soi-même (optionnel mais recommandé)
    if user == request.user:
        return redirect("manage_users")

    user.delete()
    return redirect("manage_users")



















