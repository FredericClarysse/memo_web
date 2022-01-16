from django.db import models
from django.template.defaultfilters import slugify

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
        self.slug = slugify(self.created_by.user.username) + '/' + slugify(self.name) + '/'
        super(Subject, self).save(**kwargs)


class QuestionType(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)
    question_type = models.OneToOneField(QuestionType, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return f'{self.question}'


class Answer(models.Model):
    question_ref = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    answer = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.answer}'
