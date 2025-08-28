"""Задание № 1"""

class Person:
    def __init__(self, name, age,sila):
        self.name = name
        self._age = age
        self.sila = sila

    def vozrast(self):
        if self._age > 0:
         return print(f'{self.name}, возраст: {self._age}')
        else:
            return print(f"{self._age} неправильно указан(такого не бывает)!!!")

Petrovish = Person("Petrovish", 77, 40)
baby = Person("boss_molokososs", -1, -10)
p = Person
# p.vozrast(Petrovish)
# p.vozrast(baby)

"""Задание № 2"""

class Animal:
    def __init__(self, speak):
        self.speak = speak
animal = Animal("I am an animal")
class Dog(Animal):
    def __init__(self, speak):
        super().__init__(speak)

    def Speak(self):
        print(f" Buddy: {self.speak}")
dog = Dog("woof")
print(dog.Speak())

class Сat(Animal):
    def __init__(self, speak):
        super().__init__(speak)

    def Speak1(self):
        print(f"Kitty: {self.speak}")
cat = Сat("meow")
print(cat.Speak1())

"""Задание № 3"""

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()
car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rec(Shape):
    def __init__(self, widh, heigt):
        self.widh = widh
        self.heigt = heigt
    def area(self):
        return self.widh * self.heigt

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

rect = Rec(20,6)
circle = Circle(2)

print(rect.area())
print(round(circle.area(), 2))