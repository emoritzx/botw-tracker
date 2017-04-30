"""botw-tracker quests app templatetags

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django import template

register = template.Library()

@register.filter
def in_category(things, category):
    return things.filter(quest_type=category)