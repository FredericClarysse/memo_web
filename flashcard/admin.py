from django.contrib import admin
from flashcard.models import Subject, QuestionType, Question, Answer

# Register your models here.
admin.site.register(Subject)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(Answer)
