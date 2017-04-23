#!/usr/bin/env python

# import system modules
import django
import os
import subprocess

# specify project settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'botwtracker.settings'
APP_NAME = 'botwtracker'
SETTINGS_LOCAL = 'config_local.py'

def configure_settings():
    """Configure local settings file

    Writes the settings removed from `APP_NAME/settings.py` to the localized file `SETTINGS_LOCAL`

    """
    print("Creating local settings file: %s" % SETTINGS_LOCAL)
    with open(os.path.join(APP_NAME, SETTINGS_LOCAL), "w") as f:
        for k, v in sorted(__prompt_user_settings(__get_settings_map()).items()):
            f.write("%s = %s\n" % (k, "'%s'" % v if type(v) is str else v))

def __get_settings_map():
    """Get the dictionary of localized settings w/default values
    
    Values:
        ALLOWED_HOSTS:  <empty list>
        DEBUG:          False
        LANGUAGE_CODE:  'en-us'
        SECRET_KEY:     <randomly generated key>
        TIME_ZONE:  
    
    Note:
        The secret key is generated in the same manner as the command `django-admin startapp`.
    
    """
    from django.core.management.utils import get_random_secret_key
    from django.conf.global_settings import TIME_ZONE
    return {
        'ALLOWED_HOSTS': [],
        'DEBUG': False,
        'LANGUAGE_CODE': 'en-us',
        'SECRET_KEY': get_random_secret_key(),
        'TIME_ZONE': TIME_ZONE,
    }

def __prompt_user_settings(settings):
    """Prompt the user for localized settings"""
    if input("Turn on DEBUG (not recommended for production)? [y/n] ") == 'y':
        settings['DEBUG'] = True
    host = input("Default hostname: ").strip()
    if host != '':
        settings['ALLOWED_HOSTS'].append(host)
    __prompt_user_default(settings, 'TIME_ZONE')
    __prompt_user_default(settings, 'LANGUAGE_CODE')
    return settings

def __prompt_user_default(settings, key):
    """Default prompt"""
    value = input("%s [%s]: " % (key, settings[key])).strip()
    if value != '':
        settings[key] = value
    return settings

def configure_migrations():
    """Update database schema
    
    Equivalent to running `python manage.py migrate` from the command line.

    """
    subprocess.call(["python", "manage.py", "migrate"])

def configure_quests():
    """Load quest data into database"""
    from botwtracker.settings import DATA_DIR
    from quests import loader as QuestLoader
    from quests.models import Quest
    for quest_type in Quest.QUEST_TYPES:
        with open(os.path.join(DATA_DIR, 'quests', quest_type[0] + ".dat")) as qfile:
            QuestLoader.load(qfile, quest_type[0])

def configure_testuser():
    """Load example data into database"""
    from django.contrib.auth.models import User
    user = User.objects.create_user(username='testuser', password='botw-tracker-testuser')
    from quests.models import Quest
    from user.models import QuestEntry
    import datetime
    quest=Quest.objects.all()[0]
    print(quest)
    QuestEntry(user=user.userprofile, quest=quest).save()

# run configuration
if __name__ == "__main__":
    configure_settings()
    django.setup()
    configure_migrations()
    configure_quests()
    configure_testuser()
    print("Configuration completed successfully.")