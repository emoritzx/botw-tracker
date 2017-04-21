from django.shortcuts import render
from django.http import HttpResponse
from .models import Quest

def index(request):
    quest_list = Quest.objects.order_by('quest_name')
    return render(request, 'quests/index.html', {'quest_list': quest_list})
