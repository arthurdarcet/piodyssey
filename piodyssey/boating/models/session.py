from django.core.urlresolvers import reverse
from django.contrib import admin
from django.db import models

from piodyssey.users.models import User

from .category import Category
from .question import Question


class Session(models.Model):
    class Meta:
        app_label = 'boating'

    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('api:session', args=[str(self.id)])

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
        return self.question.solution == self.answer

    def as_dict(self):
        return {
            'question': self.question.id,
            'answer': self.answer,
            'is_right': self.is_right,
        }

    def __str__(self):
        '{} ({}), {}'.format(self.answer, 'Right' if self.is_right else 'Wrong', self.question)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'created_at')


admin.site.register(Session, SessionAdmin)
