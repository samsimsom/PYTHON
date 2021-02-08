

# python da hersey birer objedir.
# siniflar class ile tanimlanir.
# class icerisinde degiskenler attribute olarak adlandirilir.
# class icerisinde function lar method olarak adlandirlir.

import random

class MyFirstClass:

    my_name = "Fırat"           # attribute
    my_surname = "Tanrıkulu"    # attribute
    my_age = "33"               # attribute

    def print_name(self):       # method
        return print(self.my_name)

    def pick_pocket(self):
        print("Called by {}".format(self))
        return bool(random.randint(0 ,1))



my_fist_class_instance = MyFirstClass()
print(my_fist_class_instance)       # <__main__.MyFirstClass object at 0x1042c7588>

my_fist_class_instance.print_name() # Fırat

my_fist_class_sec_instance = MyFirstClass()
my_fist_class_sec_instance.my_name = "Domates"

my_fist_class_sec_instance.print_name() # Domates

my_fist_class_instance.my_surname = "Kumpirim"
print(my_fist_class_instance.my_name + my_fist_class_sec_instance.my_surname)

print(my_fist_class_instance.pick_pocket())
