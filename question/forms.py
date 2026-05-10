from django import forms
from .models import Question
from tag.models import Tag

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['titre', 'description', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }