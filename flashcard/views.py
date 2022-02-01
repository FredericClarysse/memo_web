from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from flashcard.models import Subject, Card, Answer


def home(request):
    """Renders the flashcard's homepage."""
    return render(request, 'flashcard/home.html', {'title': 'Flashcard'})


def subjects(request, slug=None):
    """Renders the page with all the subjects."""
    if slug is None:
        return render(request, 'flashcard/subjects.html', {'title': 'Subject'})
    else:
        return redirect('flashcard:subject-page', slug=slug)


def subjects_ajax(request, query=None):
    """Returns a JSON containing subjects, depending on the query."""
    if query is None:
        subject_list = list(Subject.objects.filter(public=True).values('name', 'slug'))
    else:
        subject_list = list(Subject.objects.filter(public=True, name__contains=query).values('name', 'slug'))

    return JsonResponse(subject_list, safe=False)


def subject_page(request, subject_slug):
    """Returns a specific subject page."""
    subject = Subject.objects.get(slug=subject_slug)
    return render(request, 'flashcard/subject_page.html', {'title': subject.name})


def subject_testing_data(request, subject_slug):
    """Returns a JSON with the testing material (Card, possible answers and card type)."""

    cards = Card.objects.filter(subject__slug=subject_slug).all()
    print(cards)
    cards_list = []
    for card in cards:
        question_and_answers = {'card_id': card.id, 'question': card.question,
                                'card_type': card.type.name}

        possible_answers = []
        answers = Answer.objects.filter(card=card.id).all()
        for answer in answers:
            possible_answers.append(answer.answer)

        question_and_answers['possible_answers'] = possible_answers

        cards_list.append(question_and_answers)
    print(cards_list)
    return JsonResponse(cards_list, safe=False)