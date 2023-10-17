from django.core.management.base import BaseCommand
from api.bot_logic import main


class Command(BaseCommand):
    help = "Start the automated bot"

    def handle(self, *args, **options):
        main()
