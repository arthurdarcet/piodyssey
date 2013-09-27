from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return '<Category {.20!r} from {!r}>'.format(self.title, self.scraper_id)


class Question(models.Model):
    question = models.TextField()
    image = models.ImageField(upload_to='questions')
    _responseA = models.TextField(null=True)
    _responseB = models.TextField(null=True)
    _responseC = models.TextField(null=True)
    _responseD = models.TextField(null=True)
    solution = models.CharField(max_length=4, null=True)
    explanation = models.TextField(null=True)
    explanation_image = models.ImageField(upload_to='explanations')
    category = models.ForeignKey(Category)
    scraper_id = models.SlugField()

    @property
    def responses():
        res = {}
        if self._responseA is not None: res['A'] = self._responseA
        if self._responseB is not None: res['B'] = self._responseB
        if self._responseC is not None: res['C'] = self._responseC
        if self._responseD is not None: res['D'] = self._responseD
        return res
