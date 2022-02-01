from django.test import TestCase
import datetime

from flashcard.models import Subject, QuestionType, Question, Answer
from core.models import Person
from django.contrib.auth.models import User


class SubjectTestCase(TestCase):
    def setUp(self):
        """Create user, person and subject data"""
        user = User.objects.create(username='John', email='john@email.com', password='ThisIsAPassword')
        person = Person.objects.create(user=user, birthday=datetime.datetime(year=2000, month=1, day=1))
        Subject.objects.create(name='This is a subject', public=True, created_by=person)

    def test_slug_creation(self):
        """Slug has been saved correctly"""
        subject = Subject.objects.get(name='This is a subject')
        self.assertEqual(subject.slug, 'john/this-is-a-subject/')


