from django.contrib import admin
from .models import Course, Lesson, Learner, Enrollment
from .models import Question, Choice, Submission

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Course)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
