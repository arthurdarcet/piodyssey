from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

from .category import Category
from .question import Question


class Session(models.Model):
    class Meta:
        app_label = 'boating'

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def nb_errors(self):
        return len(list(a for a in self.answers.all() if not a.is_right))

    @property
    def nb_questions(self):
        return len(self.answers.all())

    @property
    def score(self):
        return self.nb_errors / self.nb_questions

    @property
    def css_status(self):
        if self.score <= 3/35:
            return 'success'
        elif self.score <= 5/35:
            return 'warning'
        else:
            return 'danger'

    def get_absolute_url(self):
        return reverse('boating:session', args=[str(self.id)])

    def get_api_url(self):
        return reverse('boating:api:session', args=[str(self.id)])

    def as_dict(self):
        return {
            'user': self.user.id,
            'created_at': str(self.created_at),
            'answers': [answer.as_dict() for answer in self.answers.all()]
        }


class Answer(models.Model):
    class Meta:
        app_label = 'boating'

    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=4)
    session = models.ForeignKey(Session, related_name='answers')

    @property
    def is_right(self):
        return sorted(self.question.solution) == sorted(self.answer)

    def as_dict(self):
        return {
            'question': self.question.id,
            'answer': self.answer,
            'is_right': self.is_right,
        }

    def __str__(self):
        return '{} ({}), {}'.format(self.answer, 'Right' if self.is_right else 'Wrong', self.question)
