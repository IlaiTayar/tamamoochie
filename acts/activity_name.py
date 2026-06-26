from enum import Enum


class ActivityName(Enum):
    EAT = "eat"
    PLAY = "play"
    WALK = "walk"
    REST = "rest"
    REVIVE = "revive"

    def __str__(self):
        return self.value