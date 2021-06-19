

from person import Person, Human

person1 = Person('ahmet', 34)
person2 = Person('kamil', 44)

print(person1.say_hello())
print(person2.say_hello())

print(person1.calculate_attack(32))
print(person2.calculate_attack(22))


human1 = Human('Devil', 340, 'Red')
print(human1.introduce())
