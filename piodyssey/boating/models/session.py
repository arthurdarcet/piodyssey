from django.core.urlresolvers import reverse
from django.db import models

from piodyssey.users.models import User

from .question import Question


class Session(models.Model):
    class Meta:
        app_label = 'boating'

    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('api:session', args=[str(self.id)])

    def as_dict(self):
        return {
            'user': self.user.id,
            'date': str(self.date),
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
        return self.question.solution == self.answer

    def as_dict(self):
        return {
            'question': self.question.id,
            'answer': self.answer,
            'is_right': self.is_right,
        }
