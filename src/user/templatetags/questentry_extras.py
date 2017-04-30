"""botw-tracker user app template tags

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django import template
from django.core.exceptions import FieldError

register = template.Library()

@register.filter
def in_category(entries, quest_type):
    try:
        return entries.filter(quest__quest_type=quest_type)
    except FieldError:
        return entries.filter(quest_type=quest_type)

@register.filter
def completion_status(entries, status):
    return entries.filter(completion_date__isnull=not status)