"""botw-tracker quests app views

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django.shortcuts import render
from .models import Quest

def index(request):
    quest_list = Quest.objects.order_by('quest_name')
    return render(request, 'quests/index.html', {'quest_list': quest_list})
