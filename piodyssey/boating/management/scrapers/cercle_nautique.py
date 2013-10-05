import bs4

from . import base_scraper


class CercleNautiqueScraper(base_scraper.BaseScraper):
    BASE_URL = 'http://www.cercle-nautique.com/m_test_permis/'
    SLUG = 'cercle-nautique'

    def categories(self):
        soup = self.soup('/')
        for td in soup.find('form').find('table').find_all('td'):
            a = td.find('a')
            yield (
                a['onclick'][33:].split(';')[0],
                a.text.split(':')[1].strip(' 12'),
                None,
            )

    def questions(self, category):
        # Initialement : POST sur http://www.cercle-nautique.com/m_test_permis/affiche-question.php
        # avec id_categorie:<cat>, action:nouveau et type_res:0
        #
        # Puis POST sur 'http://www.cercle-nautique.com/m_test_permis/affiche-question.php?id_categorie=13'
        # avec action:valid_question, bon:false, reponse[720]:0, reponse[721]:0, reponse[722]:0

        soup = self.soup('affiche-question.php', data={'action': 'nouveau', 'type_res': '0', 'id_categorie': category})

        while not soup.find(**{'class': 'bloc_resultat'}):
            qid = category + '--' + soup.find_all('h3')[1].text[11:]
            question_text = soup.find(**{'class': 'intitule'}).text

            question_image = soup.find(**{'class': 'bordPhoto'})
            if question_image:
                question_image = question_image['src']

            rids = {}
            for t in soup.find_all('script')[1].text.split('tab_')[1:]:
                t = t.split(' = ')
                rids[t[0]] = t[1].split(';')[0][-1] == '1'

            responses = {}
            solutions = ''
            for k, v in rids.items():
                txt = soup.find('input', attrs={'name': k}).previous.previous
                responses[txt[0].upper()] = txt[2:].strip()
                if v:
                    solutions += txt[0].upper()

            explanation_text = soup.find(id='explication').find_all('div')[-1].text

            yield (qid, question_text, question_image, responses, solutions, explanation_text, None)

            data = {'action': 'valid_question', 'bon': 'false'}
            for k, v in rids.items():
                data[k] = '0'
            soup = self.soup('affiche-question.php?id_categorie=' + category, data=data)
