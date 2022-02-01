from django.db import models
from django.utils.text import slugify
from random import randrange

from core.models import Person


class Subject(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    slug = models.SlugField(max_length=150, blank=True, null=False, unique=True)
    public = models.BooleanField(default=True)
    created_by = models.ForeignKey(Person, on_delete=models.CASCADE, blank=False, null=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, **kwargs):
        slug_save(self)
        super(Subject, self).save(**kwargs)


def slug_save(self):
    """Returns an unique slug"""
    if not self.slug:
        self.slug = slugify(self.name + "-" + randrange(10000, 99999, 1).__str__())
        not_unique = True
        while not_unique:
            other_slugs = type(self).objects.filter(slug=self.slug)
            if len(other_slugs) > 0:
                not_unique = True
                self.slug = slugify(self.name + "-" + randrange(10000, 99999, 1).__str__())
            else:
                not_unique = False







class CardType(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'


class Card(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)
    type = models.OneToOneField(CardType, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return f'{self.question}'


class Answer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=False, null=True)
    answer = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.answer}'
