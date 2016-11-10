# -*- coding: utf-8 -*-
from django.core.management.base import AppCommand


class Command(AppCommand):
    help = "Fills database with fake data"

    def handle_app_config(self, app_config, **options):
        pass