from django.db import models

class Quest(models.Model):
    
    STORY_TYPE = "STORY"
    SIDE_TYPE = "SIDE"
    SHRINE_TYPE = "SHRINE"
    MEMORY_TYPE = "MEMORY"
    
    QUEST_TYPES = (
        (STORY_TYPE, "Main Story Quest"),
        (SIDE_TYPE, "Side Quest"),
        (SHRINE_TYPE, "Shrine Quest"),
        (MEMORY_TYPE, "Memories")
    )

    quest_name = models.CharField(max_length=200, unique=True)
    quest_type = models.CharField(max_length=20, choices=QUEST_TYPES, default=STORY_TYPE)

    def __str__(self):
        return "%s: %s" % (self.get_quest_type_display(), self.quest_name)