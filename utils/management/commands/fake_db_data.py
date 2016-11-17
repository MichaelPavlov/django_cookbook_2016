# -*- coding: utf-8 -*-
import sys
from imp import find_module
from importlib import import_module

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Fills database with fake data"

    def handle(self, *args, **options):
        modules = self.autodiscover_module("fake_db_data")
        for module in modules:
            module.fake()

    def autodiscover_module(self, module_name, installed_apps=None):
        if installed_apps is None:
            from django.conf import settings
            installed_apps = settings.INSTALLED_APPS

        modules = []
        for app in installed_apps:
            try:
                import_module(app)
                app_path = sys.modules[app].__path__
            except AttributeError:
                continue
            try:
                find_module(module_name, app_path)
            except ImportError:
                continue
            import_module('%s.%s' % (app, module_name))
            modules.append(sys.modules['%s.%s' % (app, module_name)])

        return modules
