import bs4
import io
import logging
import os.path
import requests
import uuid

from django.core.files import File

from ...models import Category, Question


class BaseScraper:
    BASE_URL = None
    SLUG = 'base_scraper'

    def __init__(self):
        self.session = requests.Session()
        self.session.headers['User-agent'] = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'


    @property
    def logger(self):
        return logging.getLogger('scrapers.' + self.SLUG)

    def fire(self):
        for category in self.categories():
            data, category = self.save_category(*category)
            for question in self.questions(data):
                self.save_question(*question, category=category)

    def categories(self):
        # yield (data, title[, image path])
        return [(None, None)]

    def questions(self, category):
        # yield (slug, question, image path, {'A': 'response', …}, 'ACD', explanation, image path)
        raise NotImplementedError

    def request(self, path, **kwargs):
        method = 'POST' if 'data' in kwargs else 'GET'
        return self.session.request(method, self.BASE_URL + '/' + path, **kwargs)

    def soup(self, path, **kwargs):
        return bs4.BeautifulSoup(self.request(path, **kwargs).text)

    def save_category(self, data=None, title=None, image=None):
        if title is None:
            return None, None

        try:
            category = Category.objects.get(title=title)
            created = False
        except Category.DoesNotExist:
            category = Category(title=title)
            created = True

        if image is not None:
            self.set_image(category, image)

        category.save()

        self.logger.info('%s %r', ('Created' if created else 'Updated'), category)
        return data, category

    def save_question(self, slug, question_text, image, responses, solution=None, explanation=None, explanation_image=None, category=None):
        if self.SLUG is None:
            raise NotImplementedError('Scraper.SLUG needs to be set to a unique slug')
        try:
            question = Question.objects.get(slug=slug)
            created = False
        except Question.DoesNotExist:
            question = Question(slug=slug)
            created = True

        if image is not None:
            self.set_image(question, image)
        question.question = question_text
        question.category = category
        question.scraper = self.SLUG
        question.responses = responses
        question.solution = solution
        if explanation is not None:
            question.explanation = explanation
        if explanation_image is not None:
            self.set_image(question, explanation_image, 'explanation_image')

        question.save()
        self.logger.info('%s %r', ('Created' if created else 'Updated'), question)

    def set_image(self, model, image_path, image_attr='image'):
        save_to = str(uuid.uuid4()) + os.path.splitext(image_path)[1]
        getattr(model, image_attr).save(save_to, File(io.BytesIO(self.request(image_path).content)))
