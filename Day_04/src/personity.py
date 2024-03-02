#  python3 personity.py
import random


def turrets_generator():
    n = [0] * 5
    while (n[0] + n[1] + n[2] + n[3] + n[4]) != 100:
        n[0] = random.randint(0, 100)
        n[1] = random.randint(0, 100)
        n[2] = random.randint(0, 100)
        n[3] = random.randint(0, 100)
        n[4] = random.randint(0, 100)
    return n


def __init__(self):
    n = turrets_generator()
    self.neuroticism = n[0]
    self.openness = n[1]
    self.conscientiousness = n[2]
    self.extraversion = n[3]
    self.agreeableness = n[4]


def __str__(self):
    return str(
        str(self.neuroticism)
        + " "
        + str(self.openness)
        + " "
        + str(self.conscientiousness)
        + " "
        + str(self.extraversion)
        + " "
        + str(self.agreeableness)
    )


def shoot(self):
    print("Shooting")


def search(self):
    print("Searching")


def talk(self):
    print("Talking")


Turret = type(
    "Turret",
    (),
    {
        "__init__": __init__,
        "__str__": __str__,
        "shoot": shoot,
        "search": search,
        "talk": talk,
    },
)

if __name__ == "__main__":
    obj = Turret()
    obj1 = Turret()
    print(obj, "\n", obj1)
    obj.shoot()
    obj.search()
    obj.talk()
    print(obj)
