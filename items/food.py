
class Food:
    def __init__(self, food_name: str, fullness: int, power: int, health: int,
                 happiness: int):
        self.food_name = food_name
        self.fullness = fullness
        self.power = power
        self.health = health
        self.happiness = happiness


    def feed(self, tamamoochie):
        if not tamamoochie.check_fullness():
            tamamoochie.fullness += self.fullness
        else:
            tamamoochie.fullness = 100
        if not tamamoochie.check_power():
            tamamoochie.power += self.power

        else:
            tamamoochie.power = 100

        if not tamamoochie.check_health():
            tamamoochie.health += self.health

        else:
            tamamoochie.health = 5

        if not tamamoochie.check_happiness():
            tamamoochie.happiness += self.happiness

        else:
            tamamoochie.happiness = 10

        tamamoochie.power -= 10

    def __eq__(self, other):
        return self.food_name == other.food_name

    def __repr__(self):
        return f"{self.food_name}"