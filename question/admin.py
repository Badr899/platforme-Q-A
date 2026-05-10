from django.contrib import admin
from .models import Question

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation', 'score',)
    search_fields = ('titre', 'description',)
    list_filter = ( 'date_creation',)

