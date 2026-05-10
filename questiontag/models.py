from django.db import models

class QuestionTag(models.Model):
    question = models.ForeignKey(
        "question.Question",
        on_delete=models.CASCADE
    )

    tag = models.ForeignKey(
        "tag.Tag",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.question} - {self.tag}"