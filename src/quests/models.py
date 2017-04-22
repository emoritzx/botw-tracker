from django.db import models

class Quest(models.Model):
    
    STORY_TYPE = "STORY"
    SIDE_TYPE = "SIDE"
    SHRINE_TYPE = "SHRINE"
    
    QUEST_TYPES = (
        (STORY_TYPE, "Main Story Quest"),
        (SIDE_TYPE, "Side Quest"),
        (SHRINE_TYPE, "Shrine Quest")
    )

    quest_name = models.CharField(max_length=200)
    quest_type = models.CharField(max_length=20, choices=QUEST_TYPES, default=STORY_TYPE)