# -*- coding: utf-8 -*-

## Lists

items_list = ['knife', 'rifle', 'bottle', 'rope', 'torch']

print(items_list)
# listedeki eleman sayisi. len()
print( len(items_list) )
# listenin ilk elemanına erişmek.list_name[0]
print( items_list[0] )
# listenin son elemanına ulaşmak. list_name[-1]
print( items_list[-1] )
# listenin elemanrı dışında bir index numarası girersen. hata verir.
try:
    print( items_list[5] ) # item_list son index numarası 4.
except IndexError:
    print('Bu index numaralı bir eleman yok.')

# listede kesit alma. Slicing.
print( items_list[0:2] ) # sagdaki index numarası dahil edilmez.

# listenin son elemanınıda göstermek isteseydim.
print( items_list[1:5] ) # liste uzunlugu len() kadar deger girmeliyim.

# listenin sonuna gitmesini istersem daha pratik bir yol.
print( items_list[2:] ) # sag tarafa rakam girmiyorum.

backpack_list = ['apple', 'bread', 'banana', 'watermelon']
# .append() metodu
print( backpack_list )
backpack_list.append('kiwi')
print( backpack_list )
# listenin istedigim indexine yerleştirmek için. 
backpack_list.insert(1, 'oranges')
print(backpack_list)
# baska bir list ile genişletmek.
backpack_list.extend(items_list)
print(backpack_list)

# listeden element çıkartmak isimle. .remove('name')

backpack_list.remove('knife')
print(backpack_list)

# listenin son elemanını çıkartır ve döndürür.

list_last_obj = backpack_list.pop()
print(backpack_list)
print(list_last_obj)

# Listeyi ters cevirmek için. reverse()

shopping_list = ['apple', 'tursu', 'barbunya']
shopping_list.reverse()
print(shopping_list)

# siralamak için. sort()
# eger siralanmis ve ters cevrilmis olmasini istersen. sort(reverse=True)
numbers = [1, 6, 9, 3, 6, 0]
numbers.sort()
print(numbers)

alphabet = ['a', 'x', 't', 'e', 'f']
alphabet.sort(reverse=True)
print(alphabet)

# Eger listenin siralnmış bir versiyonunu istersen. sorted()
# liste degişmez. digerlerinde listler degiştirilir.

sec_numbers = [2, 5, 1, 67, -1]
print(sec_numbers)
sorted_sec_numbers = sorted(sec_numbers)
print(sorted_sec_numbers)

# liste elemtlerinin max(), min() ve sum() gibi fonksyonlar ile
# min ve max degerleri bulunabilir, tüm degerleri toplanabilir.
# min ve max stringler içinde çalışır fakat sum() çalışmaz.

print(min(sec_numbers))
print(max(sec_numbers))
print(sum(sec_numbers))

print(min(backpack_list))
print(max(backpack_list))

# listelerin index ve degerlerine ulaşmak istersen. enumarate()
# gerçek dünya sıralaması gibi görünmesini istersen. enumarate(start=!)

courses = ['Math', 'History', 'Art', 'CompSci']

for index, course in enumerate(courses, start=1):
    print(index, course)

# liste elemanlarını, str haline getiriyor.
courses_str = ' - '.join(courses)
print(courses_str)
# stringleri kuralına göre bölüp liste haline getiriyor.
new_course_list = courses_str.split(' - ')
print(new_course_list)

"""
You have to understand that Python represents all its data as objects.
Some of these objects like lists and dictionaries are mutable,
meaning you can change their content without changing their identity.
Other objects like integers, floats, strings and tuples are objects
that can not be changed.
"""

## Empty List
empty_list = []
empty_list = list()

## Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

## Empty Sets
empty_set = set()

## Empty Dictionary {}

