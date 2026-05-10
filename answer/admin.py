from django.contrib import admin
from .models import Answer

# Register your models here.

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'question', 'date_creation', 'est_acceptee', 'score')
    search_fields = ('contenu',)
    list_filter = ( 'date_creation',)
