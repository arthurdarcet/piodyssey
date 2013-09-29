from django.core.urlresolvers import reverse
from django.db import models

from .question import Question
from .user import User


class Session(models.Model):
    class Meta:
        app_label = 'piodyssey'

    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    def as_dict(self):
        return {
            user: self.user.id,
            date: self.date,
            answers: [answer.as_dict() for answer in self.answers]
        }


class Answer(models.Model):
    class Meta:
        app_label = 'piodyssey'

    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=4)
    session = models.ForeignKey(Session)

    @property
    def is_right(self):
        return self.question.solution == self.answer

    def get_absolute_url(self):
        return reverse('get-session', args=[str(self.id)])

    def as_dict(self):
        return {
            question: self.question.id,
            answer: self.answer
        }
