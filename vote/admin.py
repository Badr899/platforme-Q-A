from django.contrib import admin
from .models import Vote

# Register your models here.

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_vote', 'question', 'answer')
    list_filter = ('type_vote',)