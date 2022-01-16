from django.shortcuts import render

from flashcard.models import Subject


def home(request):
    return render(request, 'flashcard/home.html', {'title': 'Flashcard'})


def subjects(request, query):
    if query == 'all':
        subject_objects = Subject.objects.filter(public=True)
    else:
        subject_objects = Subject.objects.filter(name=query, public=True)
    return render(request, 'flashcard/subjects.html', {'title': 'Subject', 'subjects': subject_objects})