import optparse

from django.core.management.base import BaseCommand, CommandError

from .. import scrapers


class Command(BaseCommand):
    args = '<scraper_id scraper_id ...>'
    help = 'Closes the specified poll for voting'

    option_list = BaseCommand.option_list + (
        optparse.make_option('--all',
            action='store_true',
            default=False,
            help='Use all available scrapers'),
        )

    SCRAPERS = {
        'loisirs_nautic': scrapers.LoisirsNauticScraper,
        'cercle_nautique': scrapers.CercleNautiqueScraper,
    }

    def handle(self, *args, **options):
        if options['all']:
            args = self.SCRAPERS.keys()
        for scraper_id in args:
            if scraper_id not in self.SCRAPERS:
                raise CommandError('Unknown scraper ID {}'.format(scraper_id))
            self.SCRAPERS[scraper_id]().fire()
