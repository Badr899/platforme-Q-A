from .models import Tag
from django.shortcuts import render, redirect, get_object_or_404
from question.models import Question
from .forms import TagForm

def manage_tags(request):

    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manage_tags')

    else:
        form = TagForm()

    tags = Tag.objects.all()

    return render(request, "admin/tags.html", {
        "tags": tags,
        "form": form
    })


def tag_detail(request, id):
    tag = get_object_or_404(Tag, id=id)

    questions = Question.objects.filter(tags=tag).order_by('-date_creation')

    return render(request, "tags/tag_detail.html", {
        "tag": tag,
        "questions": questions
    })


def delete_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag.delete()
    return redirect('manage_tags')


def update_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            return redirect('manage_tags')

    else:
        form = TagForm(instance=tag)

    return render(request, "admin/edit_tag.html", {
        "form": form
    })