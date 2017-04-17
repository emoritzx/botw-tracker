from quests.models import Quest

def load(fstream, quest_type):
    print("Loading %s quests..." % quest_type)
    for line in fstream:
        quest = Quest(quest_name=line.strip(), quest_type=quest_type)
        quest.save()