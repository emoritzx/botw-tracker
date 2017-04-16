from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from quests.models import QuestEntry

class QuestInline(admin.StackedInline):
    model = QuestEntry

class UserAdmin(BaseUserAdmin):
    inlines = (QuestInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)