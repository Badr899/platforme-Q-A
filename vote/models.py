from django.db import models
from django.conf import settings

class Vote(models.Model):
    TYPE_CHOICES = [
        ("up", "Positif"),
        ("down", "Négatif"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="votes"
    )

    question = models.ForeignKey(
        "question.Question",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="votes"
    )

    answer = models.ForeignKey(
        "answer.Answer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="votes"
    )

    type_vote = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        cible = self.question or self.answer
        return f"Vote {self.type_vote} de {self.user} sur {cible}"