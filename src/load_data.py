# specify project settings
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'botwtracker.settings'

# initialize django
import django
django.setup()

# import project
from botwtracker.settings import DATA_DIR
from quests import loader as QuestLoader
from quests.models import Quest

# run loaders
if __name__ == "__main__":
    print("Hello World")
    for quest_type in Quest.QUEST_TYPES:
        with open(os.path.join(DATA_DIR, 'quests', quest_type[0] + ".dat")) as qfile:
            QuestLoader.load(qfile, quest_type[0])