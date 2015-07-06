from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from provider.oauth2.models import Client

from oauth2_provider.models import TrustedClient


class Command(BaseCommand):
    args = 'url redirect_uri client_id client_secret client_type'
    help = 'Create a new OAuth2 Client.'

    option_list = BaseCommand.option_list + (
        make_option(
            '-i',
            '--client_id',
            action='store',
            type='string',
            dest='client_id',
            help="String to assign as the Client ID."
        ),
        make_option(
            '-s',
            '--client_secret',
            action='store',
            type='string',
            dest='client_secret',
            help="String to assign as the Client Secret. Should not be shared."
        ),
        make_option(
            '-t',
            '--trusted',
            action='store_true',
            dest='trusted',
            default=False,
            help="Designate the Client as trusted. Trusted Clients bypass the user consent "
                 "form typically displayed after validating the user's credentials."
        ),
    )

    def handle(self, *args, **options):
        try:
            client = Client.objects.create(foo=foo, bar=baz)
        except:
            raise CommandError("Clunk.")

        self.stdout.write("Created OAuth2 Client...")
