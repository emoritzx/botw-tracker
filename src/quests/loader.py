"""botw-tracker quests app database loader

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from quests.models import Quest

def load(fstream, quest_type):
    print("Loading %s quests..." % quest_type)
    for line in fstream:
        quest_name = line.strip()
        try:
            quest = Quest(quest_name=quest_name, quest_type=quest_type)
            quest.save()
            print("%s quest '%s' saved." % (quest_type, quest_name))
        except:
            print("Skipping %s quest: %s" % (quest_type, quest_name))