from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Migrate the all databases at once'

    def handle(self, *args, **options):
        call_command("migrate")
        call_command("migrate", "--database=payments")

        self.stdout.write(self.style.SUCCESS('Successfully migrated databases'))
