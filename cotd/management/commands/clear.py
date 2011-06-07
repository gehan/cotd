from django.core import management
from django.core.management.base import NoArgsCommand
from django.core.management.commands.syncdb import Command as SyncCommand
from django.conf import settings
from django.db import connection 
from optparse import make_option
from cotd.management import setup_data

class Command(NoArgsCommand):
    help = "Drops and recreates the database and loads initial set of data"

    def handle_noargs(self, **options):
        cursor = connection.cursor()
        cursor.execute("DROP DATABASE `%s`"%settings.DATABASES['default']['NAME'])
        cursor.execute("CREATE DATABASE `%s` CHARACTER SET='utf8' COLLATE='utf8_general_ci'"%settings.DATABASES['default']['NAME'])
        cursor.execute("USE `%s`"%settings.DATABASES['default']['NAME'])
        sync = SyncCommand()
        sync.handle_noargs()
        setup_data.setup()