
# class lar functionlar gibi calistirilmazlar.
# Basit Role Playing game

import random

## --- C L A S S --- ##

class Thief:

     def __init__(self, name, sneaky=True, **kwargs):
         self.name = name
         self.sneaky = sneaky

         for attribute, value in kwargs.item():
             setattr(self, attribute, value)


     def pickpocket(self):
         return self.sneaky and bool(random.randint(0, 1))


     def hide(self, light_level):
         return self.sneaky and light_level < 10


## --- C L A S S --- ##

# samsim = Thief()
# print(samsim.sneaky)
#
# ahmet = Thief
# ahmet.sneaky = False            # class instance, attribute degistiriyorum.
# print(ahmet.sneaky)
#
# print(Thief.sneaky)             # Class in kendi attribute u.