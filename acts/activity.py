from abc import ABC, abstractmethod

from acts.activity_name import ActivityName


class Activity(ABC):

    @abstractmethod
    def __init__(self, activity_name: ActivityName):
        self.activity_name = activity_name

    @abstractmethod
    def act(self):
        pass


