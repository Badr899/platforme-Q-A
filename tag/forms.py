from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nom']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')

        if len(nom) < 2:
            raise forms.ValidationError("Le nom du tag est trop court")

        return nom