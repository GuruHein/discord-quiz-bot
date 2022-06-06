from django.contrib import admin
from . models import Question, Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'points', 'difficulty', 'is_active')
    list_filter = ('difficulty', 'is_active')
    search_fields = ('title',)
    inlines = [AnswerInline]


@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_correct', 'created_at', 'updated_at')
    list_filter = ('is_correct', 'created_at', 'updated_at')
    search_fields = ('question__id', 'answer')

