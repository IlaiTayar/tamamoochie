from acts.activity_name import ActivityName
from items.food import Food
from tms.tamamoochie import Tamamoochie
from tms.tm_type import TmType


class Cat(Tamamoochie):
    def __init__(self,tm_name: str, favorite_activity: ActivityName, favorite_food: Food):
        super().__init__(TmType.CAT, tm_name, favorite_activity, favorite_food)

