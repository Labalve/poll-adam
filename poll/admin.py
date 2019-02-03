from django.contrib import admin
from .models import QuestionSet, Question, Choice, Answer

# Register your models here.
admin.site.register(Choice)
admin.site.register(Answer)


class InlineChoice(admin.TabularInline):
    model = Choice


class InlineQuestion(admin.TabularInline):
    model = Question


class QuestionSetAdmin(admin.ModelAdmin):
    inlines = [
        InlineQuestion,
    ]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        InlineChoice,
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSet, QuestionSetAdmin)
