from django.db import models
from django.contrib import admin

from . import Category


class Question(models.Model):
    class Meta:
        app_label = 'piodyssey'
        unique_together = (
            ('slug', 'scraper'),
        )

    question = models.TextField()
    image = models.ImageField(upload_to='questions')
    _responseA = models.TextField(null=True)
    _responseB = models.TextField(null=True)
    _responseC = models.TextField(null=True)
    _responseD = models.TextField(null=True)
    solution = models.CharField(max_length=4, null=True)
    explanation = models.TextField(null=True)
    explanation_image = models.ImageField(upload_to='explanations')
    category = models.ForeignKey(Category, null=True)
    scraper = models.SlugField()
    slug = models.SlugField()

    @property
    def responses(self):
        res = {}
        if self._responseA is not None: res['A'] = self._responseA
        if self._responseB is not None: res['B'] = self._responseB
        if self._responseC is not None: res['C'] = self._responseC
        if self._responseD is not None: res['D'] = self._responseD
        return res

    @responses.setter
    def responses(self, responses):
        if 'A' in responses: self._responseA = responses['A']
        if 'B' in responses: self._responseB = responses['B']
        if 'C' in responses: self._responseC = responses['C']
        if 'D' in responses: self._responseD = responses['D']

    def __str__(self):
        return '{!r} {!r} in {} from {!r}'.format(self.slug, self.question[:20], self.category, self.scraper)

    def as_dict(self):
        return {
            'question': self.question,
            'image': self.image.url if self.image else None,
            'responses': self.responses,
            'explanation': self.explanation,
            'explanation_image': self.explanation_image.url if self.explanation_image else None,
            'id': self.pk,
            'solution': self.solution,
        }


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('slug', 'question', 'category', 'scraper')
    list_filter = ('category', 'scraper')
    search_fields = ('question', '_responseA', '_responseB', '_responseC', '_responseD')
    ordering = ('scraper', 'category', 'slug')
admin.site.register(Question, QuestionAdmin)

