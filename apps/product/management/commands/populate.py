from django.core.management.base import BaseCommand
from libs.populate import populate
from libs.depopulate import depopulate
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Populates database with products and superuser"

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.count() > 0:
            depopulate()
            self.stdout.write(self.style.SUCCESS(
                'Database has been reset. '
                '\n Populating database with data...'
            ))

        populate()
        self.stdout.write(self.style.SUCCESS(
            'Database population completed.'
        ))
