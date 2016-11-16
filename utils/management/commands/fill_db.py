# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from movies.tests.factories import fill_db


class Command(BaseCommand):
    help = "Fills database with fake data"

    def handle(self, *args, **options):
        fill_db()
