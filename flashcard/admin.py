from django.contrib import admin
from flashcard.models import Subject, CardType, Card, Answer

# Register your models here.
admin.site.register(Subject)
admin.site.register(CardType)
admin.site.register(Card)
admin.site.register(Answer)
