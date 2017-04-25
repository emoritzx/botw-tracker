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

    def get_quest_types(self):
        return Quest.QUEST_TYPES

class UserProfileUpdate(LoginRequiredMixin, RedirectView):

    login_url = reverse_lazy('login')
    pattern_name = 'app-views-user'

    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        action = self.request.GET.get('action')
        entry = self.request.GET.get('entry')
        if not action:
            raise SuspiciousOperation('No action provided')
        if action == 'complete':
            if not entry:
                raise SuspiciousOperation('No entry provided')
            entry_obj = QuestEntry.objects.get(pk=entry)
            if entry_obj.user.user.id != user.id:
                raise SuspiciousOperation('Quest entry does not belong to user')
            entry_obj.completion_date = timezone.now()
            entry_obj.save(update_fields=['completion_date'])
        return super().get_redirect_url(*args, slug=user.username)