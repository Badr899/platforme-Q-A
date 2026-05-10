from django.db import models
from django.conf import settings

class Comments(models.Model):
    contenu = models.TextField()

    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments"
    )

    question = models.ForeignKey(
        "question.Question",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="comments"
    )

    answer = models.ForeignKey(
        "answer.Answer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="comments"
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cible = self.question or self.answer
        return f"Commentaire de {self.auteur} sur {cible}"