"""botw-tracker user app views

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from .models import UserProfile, QuestEntry
from quests.models import Quest

def index(request):
    user_list = UserProfile.objects.order_by('user__username')
    return render(request, 'user/index.html', {'user_list': user_list})

class UserProfileView(DetailView):

    model = UserProfile
    slug_field = "user__username"

    def get_user_id(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except KeyError:
            user = User.objects.get(username=self.kwargs['slug'])
        return user.id

    def get_quest_types(self):
        return Quest.QUEST_TYPES

    def get_undiscovered_quests(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except KeyError:
            user = User.objects.get(username=self.kwargs['slug'])
        quests = [entry.quest.id for entry in QuestEntry.objects.filter(user__user=user)]
        return Quest.objects.exclude(id__in=quests)

class UserProfileUpdate(LoginRequiredMixin, RedirectView):

    login_url = reverse_lazy('login')
    pattern_name = 'app-views-user'

    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        action = self.request.POST.get('action')
        id = self.request.POST.get('id')
        if action == 'complete':
            entry_obj = self.verify_entry(user, id)
            entry_obj.completion_date = timezone.now()
            entry_obj.save(update_fields=['completion_date'])
        elif action == 'discover':
            quest = Quest.objects.get(pk=id)
            profile = UserProfile.objects.get(user=user)
            QuestEntry.objects.create(user=profile, quest=quest)
        elif action == 'remove':
            entry_obj = self.verify_entry(user, id)
            entry_obj.delete()
        elif action == 'downgrade':
            entry_obj = self.verify_entry(user, id)
            entry_obj.completion_date = None
            entry_obj.save(update_fields=['completion_date'])
        else:
            raise SuspiciousOperation('Unknown action: %s' % action)
        return super().get_redirect_url(*args, slug=user.username)

    def verify_entry(self, user, id):
        if not id:
            raise SuspiciousOperation('No entry provided')
        entry_obj = QuestEntry.objects.get(pk=id    )
        if entry_obj.user.user.id != user.id:
            raise SuspiciousOperation('Quest entry does not belong to user')
        return entry_obj