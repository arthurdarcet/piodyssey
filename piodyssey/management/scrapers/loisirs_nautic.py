import bs4

from . import base_scraper


class LoisirNauticScraper(base_scraper.BaseScraper):
    BASE_URL = 'http://www.loisirs-nautic.fr/'
    SLUG = 'loisirs-nautic'

    def categories(self):
        soup = self.soup('tests-permis-cotier.php')
        for tr in soup.find(id='tabs-1').find_all('table')[1].children:
            if isinstance(tr, bs4.Tag):
                links = tr.find_all('a')
                yield (links[0]['href'], links[1].text, tr.find('img')['src'])

    def _questions_ids(self, category):
        soup = self.soup(category)
        for question in soup.find_all(**{'class': 'gobas'}):
            # js = document.getElementById('submit').click();affiche_correction('PC2',2);
            js = question.find_all('a')[1]['onclick']
            yield js[62:].split("'", 1)[0] # yield 'PC2'

    def questions(self, category):
        for qid in self._questions_ids(category):
            soup = self.soup('pgm/affiche_correction.php?id=' + qid)

            question = soup.find(**{'class': 'quest'})
            question_text = question.find('h6').text.strip()
            img = question.find('img')
            question_image = img['src'] if img is not None else None

            responses = {}
            solutions = ''
            for resp in question.find('form').find_all('p'):
                rid, rtxt = resp.text.split(' - ', 1)
                responses[rid] = rtxt
                if 'checked' in resp.find('input').attrs:
                    solutions += rid

            explanation = soup.find(**{'class': 'gratuit'})
            p = explanation.find('p')
            explanation_text = p.text[35:].strip() if p is not None else None
            images = explanation.find_all('img')
            explanation_image = images[1]['src'] if len(images) > 1 else None

            yield (qid, question_text, question_image, responses, solutions, explanation_text, explanation_image)

