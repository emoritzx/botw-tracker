from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from quests.models import Quest

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

class QuestEntry(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    discovery_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True)

    def completed(self):
        return self.completion_date != None

def __create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(__create_user_profile, sender=User)
