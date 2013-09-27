import bs4
import logging
import urllib.request


logger = logging.getLogger(__name__)

class BaseScraper:
    BASE_URL = None

    def fire(self):
        for category in self.categories():
            data, cid = self.save_category(*category)
            for question in self.questions(data):
                self.save_question(*question, category_id=cid)

    def categories(self):
        # yield (data, title[, image path])
        return [(None, None)]

    def questions(self, category):
        # yield ((question[, image path]), {'A': 'response', …}[, 'ACD'[, (explanation[, image path])]])
        raise NotImplementedError

    def get_image(self, img):
        filename, _ = urllib.request.urlretrieve(self.BASE_URL + '/' + img)
        return filename

    def soup(self, path):
        with urllib.request.urlopen(self.BASE_URL + '/' + path) as f:
            return bs4.BeautifulSoup(f.read())

    def save_category(self, data=None, title=None, image=None):
        if title is None:
            return None
        logger.info('Creating category %r, data: %r, image: %r', title, data, image)
        # TODO
        return data, 0

    def save_question(self, question, responses, solution=None, explanation=None, category_id=None):
        logger.info('Creating question %.20s in category %s, solution: %s, explanation: %.20s', question[0], category_id, solution, explanation[0])
