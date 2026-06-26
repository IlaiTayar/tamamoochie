from acts.activity_name import ActivityName
from acts.eat import Eat
from items.food import Food
from tms.cat import Cat

if __name__ == '__main__':
    kibble = Food("bonzo", 15, 10, 0, 0)
    kibbl = Food("bon", 15, 10, 0, 0)
    kibb = Food("bonz", 15, 10, 0, 0)
    cat1 = Cat("mitzi", ActivityName.EAT, kibble)
    cat2 = Cat("mitz", ActivityName.PLAY, kibble)
    cat3 = Cat("mit", ActivityName.EAT, kibble)
    cat1.power = 80
    cat1.happiness = 8
    eat1 = Eat(cat1)
    print()
    eat1.add_food([kibble, kibbl, kibb])
    print()
    eat1.act()
    print()
    eat2 = Eat(cat2)
    print()
    eat2.add_food([kibbl, kibb, kibble])
    print()
    eat2.act()
    print()
    eat3 = Eat(cat3)
    print()
    eat3.add_food(kibb)
    print()
    eat3.act()
