from django.db import models
from django.conf import settings


class Answer(models.Model):
    contenu = models.TextField()

    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="answers"
    )

    question = models.ForeignKey(
        "question.Question",
        on_delete=models.CASCADE,
        related_name="answers"
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    est_acceptee = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Answer {self.pk}"