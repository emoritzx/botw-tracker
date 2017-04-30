"""WSGI config for botwtracker project.

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

It exposes the WSGI callable as a module-level variable named ``application``.

"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "botwtracker.settings")
application = get_wsgi_application()