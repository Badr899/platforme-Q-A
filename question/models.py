from django.db import models
from django.conf import settings


class Question(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()

    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="questions"
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    views = models.IntegerField(default=0)

    tags = models.ManyToManyField(
        "tag.Tag",
        through="tag.QuestionTag",
        related_name="questions"
    )


    def __str__(self):
        return self.titre