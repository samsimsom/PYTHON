

from random import randint


class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f'Hello, my name is {self.name}'

    def calculate_attack(self, damege) -> int:
        random_number = randint(0, 30)
        result = damege + random_number
        return result


class Human(Person):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.color = color

    def introduce(self):
        return f'My name is {self.name},' \
               f'Im {self.age} years old.' \
               f'My favorite color is {self.color}'
