from abc import ABC, abstractmethod

from acts.activity_name import ActivityName
from items.food import Food
from tms.tm_type import TmType


class Tamamoochie(ABC):

    @abstractmethod
    def __init__(self, tm_type: TmType, tm_name: str,
                 favorite_activity: ActivityName, favorite_food: Food):
        self.tm_type = tm_type
        self.tm_name = tm_name
        self.favorite_activity = favorite_activity
        self.favorite_food = favorite_food
        self.health = 5
        self.happiness = 10
        self.power = 100
        self.fullness = 100


    def is_alive(self):
        if self.health <= 0:
            print(f"your Tamatoochie {self.tm_name} has sadly passed away R.I.P")
            return False
        else:
            return True


    def set_health(self):
        if (self.happiness <= 0 and self.fullness <= 20) or (self.happiness <= 0 and self.power <= 20):
            self.health -= 1
        elif self.power <= 0 or self.fullness <= 0:
            self.health -= 2
        elif self.happiness <= 0 and self.fullness <= 0 and self.power <= 0:
            self.health = 0
        return self.is_alive()



    def check_health(self):
        max_health = 4

        return self.health > max_health

    def check_happiness(self):
        max_happiness = 8

        return self.happiness > max_happiness

    def check_power(self):
        max_power = 80

        return self.power > max_power

    def check_fullness(self):
        max_fullness = 90

        return self.fullness > max_fullness



    def __str__(self):
        return (f"=== tamamoochie data ==="
                f"\ntype: {self.tm_type}"
                f"\nname: {self.tm_name}"
                f"\nfavorite activity: {self.favorite_activity}"
                f"\nfavorite food: {self.favorite_food}"
                f"\n=== current stats ==="
                f"\nhealth: {self.health}"
                f"\nhappiness: {self.happiness}"
                f"\npower: {self.power}"
                f"\nfullness: {self.fullness}")

    def __repr__(self):
        return f"{self.tm_type} {self.tm_name}"

    def __eq__(self, other):
        return (self.tm_type, self.tm_name) == (other.tm_type, other.tm_name)


