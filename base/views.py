from multiprocessing import context

from django.views.generic import TemplateView
from question.models import Question
from tag.models import Tag
from django.db.models import Count, Q

class HomeView(TemplateView):
    template_name = "base/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get("q")  # 🔥 récupération recherche

        questions = Question.objects.all().prefetch_related("votes")

        # 🔍 FILTRE PAR TAG (ou titre si tu veux)
        if query:
            questions = questions.filter(
                Q(tags__nom__icontains=query) |
                Q(titre__icontains=query)
            ).distinct()
        
        if not questions.exists():
            no_result = True

            context["no_result"] = no_result


        # 🔥 calcul score
        for q in questions:
            q.upvotes = q.votes.filter(type_vote="up").count()
            q.downvotes = q.votes.filter(type_vote="down").count()
            q.score = q.upvotes - q.downvotes

        context["questions"] = questions
        context["tags"] = Tag.objects.all()[:15]

        context["tag_count"] = Tag.objects.count()
        context["question_count"] = Question.objects.count()

        context["query"] = query  # 🔥 pour garder dans input

        return context