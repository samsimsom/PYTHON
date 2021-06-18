

from random import randint


class Person(object):
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f'Hello, my name is {self.name}'

    def calculate_attack(self, damege) -> int:
        random_number = randint(0, 30)
        result = damege + random_number
        return result
