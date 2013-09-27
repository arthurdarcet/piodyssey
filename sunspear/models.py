from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return '{!r}'.format(self.title[:20])


class Question(models.Model):
    class Meta:
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
