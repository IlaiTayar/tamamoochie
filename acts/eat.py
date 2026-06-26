from acts.activity import Activity
from acts.activity_name import ActivityName
from items.food import Food
from tms.tamamoochie import Tamamoochie


class Eat(Activity):
    def __init__(self,tamamoochie: Tamamoochie):
        super().__init__(ActivityName.EAT)
        self.food = []
        self.tamamoochie = tamamoochie


    def act(self):
        if self.tamamoochie.set_health():
            print(f"initializing {self.activity_name}."
                  f"\n{self.tamamoochie.tm_name} is looking for food..."
                  f"\n available food: {self.food}\n")

            if self.tamamoochie.favorite_activity == self.activity_name:
                print(f"its {self.tamamoochie.tm_name}'s favorite activity!")

                if self.tamamoochie.check_happiness():
                    print(f"{self.tamamoochie.tm_name} is OVERJOYED!\n")

                else:
                    self.tamamoochie.happiness += 2
                    print(f"{self.tamamoochie.tm_name} got a HAPPINESS BOOST!"
                          f"\n{self.tamamoochie.tm_name}'s happiness is: {self.tamamoochie.happiness}.\n")

                if self.tamamoochie.favorite_food in self.food:
                    print(f"{self.tamamoochie.tm_name} found his favorite food!")

                    if self.tamamoochie.check_power():
                        print(f"{self.tamamoochie.tm_name} is FULL OF POWER!\n")

                    else:
                        self.tamamoochie.power += 20
                        print(f"{self.tamamoochie.tm_name} got a POWER BOOST!"
                              f"\n{self.tamamoochie.tm_name}'s power is: {self.tamamoochie.power}.\n")

                    for i in range(len(self.food)):
                        if self.food[i].food_name == self.tamamoochie.favorite_food.food_name:
                            self.food[i].feed(self.tamamoochie)
                            del self.food[i]
                            print(f"{self.tamamoochie.tm_name} is done eating his favorite food!\n")
                            break

                if len(self.food) > 0:
                    print(f"{self.tamamoochie.tm_name} could not find his favorite food "
                          f"and will it the first item he finds.")
                    self.food[0].feed(self.tamamoochie)
                    del self.food[0]
                    print(f"{self.tamamoochie.tm_name} is done eating\n")

            elif self.tamamoochie.favorite_food in self.food:
                print(f"{self.tamamoochie.tm_name} found his favorite food!")

                if self.tamamoochie.check_power():
                    print(f"{self.tamamoochie.tm_name} is FULL OF POWER!\n")

                else:
                    self.tamamoochie.power += 20
                    print(f"{self.tamamoochie.tm_name} got a POWER BOOST!"
                          f"\n{self.tamamoochie.tm_name}'s power is: {self.tamamoochie.power}.\n")

                for i in range(len(self.food)):
                    if self.food[i].food_name == self.tamamoochie.favorite_food.food_name:
                        self.food[i].feed(self.tamamoochie)
                        del self.food[i]
                        print(f"{self.tamamoochie.tm_name} is done eating his favorite food!\n")
                        break

            else:
                if len(self.food) > 0:
                    print(f"{self.tamamoochie.tm_name} could not find his favorite food "
                          f"and will it the first item he finds.")
                    self.food[0].feed(self.tamamoochie)
                    del self.food[0]
                    print(f"{self.tamamoochie.tm_name} is done eating\n")

            self.tamamoochie.set_health()
            print(f"food left: {self.food}")


    def add_food(self, food: Food | list[Food]):

        print(f"current food in stock: {self.food}")

        if type(food) == Food:
            self.food.append(food)

        else:
            for i in range(len(food)):
                self.food.append(food[i])
        print(f"current food in stock: {self.food}")
