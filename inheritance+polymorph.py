class Sex:
    MALE = "male"
    FEMALE = "female"


class Human:
    def __init__(self, name, sex, pos=(0, 0)) -> None:
        self.name = name
        self.sex = sex
        self.pos = pos

    def move(self, direction=(0, 0)):
        self.pos = direction

    def talk(self, sound=""):
        print(sound)


class Pilot(Human):
    def fly(self): ...


class MilitaryPilot(Pilot):
    def shoot(self, target): ...

class Vehicle:
    def move(self, **kwargs): ...
    
class Car(Vehicle):
    def move(self, point_a, point_b): ...

class Plane(Vehicle):
    ...
    
class WarPlane(Plane):
    ...
    
class Bike(Vehicle):
    def move(self, point_a, point_b): ...

class Driver(Human):
    def drive(self, car: Car): ...

class Warrior(Human):
    def search(self, target_types): ...
    def destroy(self, target): ...
    
    
class HumanStatistic(Human):
    count = 0

    def __init__(self, name, sex, pos=(0, 0)) -> None:
        HumanStatistic.count += 1
        self.op_id = HumanStatistic.count
        super().__init__(name, sex, pos)

    def __del__(self) -> None:
        HumanStatistic.count -= 1
        # super().__del__()


b = [
    HumanStatistic("Sara", Sex.FEMALE),
    Human("Jhon", Sex.MALE),
    Human("Olga", Sex.FEMALE),
    HumanStatistic("Mattew", Sex.MALE),
]

for people in b:
    if isinstance(people, Human):
        people.talk(f"My name is {people.name}. I'm {people.sex}")
    if isinstance(people, HumanStatistic):
        print(f"My op_id :>> {people.op_id}")
