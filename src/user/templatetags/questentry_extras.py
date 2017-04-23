from django import template

register = template.Library()

@register.filter
def in_category(entries, quest_type):
    return entries.filter(quest__quest_type=quest_type)

@register.filter
def completion_status(entries, status):
    return entries.filter(completion_date__isnull=not status)